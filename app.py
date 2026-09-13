"""
AyurDiag — AI-Powered Ayurvedic & Medical Assistant
Flask Backend with RAG Pipeline using SentenceTransformers + ChromaDB
"""

import os
import re
import sys
import shutil
import torch
import openpyxl
import chromadb
from flask import Flask, render_template, request, jsonify
from sentence_transformers import SentenceTransformer
from datetime import datetime

# Windows console (cp1252) cannot encode emoji in print() output.
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ──────────────────────────────────────────────
# Flask App Initialization
# ──────────────────────────────────────────────
app = Flask(__name__)

# ──────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────
DATASET_PATH = os.path.join(os.path.dirname(__file__), "Final Year Diseases Dataset.xlsx")
CHROMA_DIR = os.path.join(os.path.dirname(__file__), "chroma_db")
MODEL_NAME = "all-MiniLM-L6-v2"
COLLECTION_NAME = "diseases"
TOP_K = 3

# ──────────────────────────────────────────────
# Device Detection
# ──────────────────────────────────────────────
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"🖥  Device: {device}")

# ──────────────────────────────────────────────
# Load SentenceTransformer Model
# ──────────────────────────────────────────────
print(f"📦 Loading embedding model: {MODEL_NAME} ...")
embedder = SentenceTransformer(MODEL_NAME, device=device)
print("✅ Embedding model loaded.")

# ──────────────────────────────────────────────
# Load & Preprocess Dataset
# ──────────────────────────────────────────────
def load_dataset(path: str) -> list[dict]:
    """Load the diseases dataset from an Excel file."""
    wb = openpyxl.load_workbook(path, read_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(min_row=2, values_only=True))
    wb.close()

    records = []
    for row in rows:
        if not row or not row[0]:
            continue
        disease = str(row[0]).strip()
        symptoms = str(row[1]).strip() if row[1] else ""
        ayurvedic = str(row[2]).strip() if row[2] else ""
        allopathic = str(row[3]).strip() if row[3] else ""
        advice = str(row[4]).strip() if len(row) > 4 and row[4] else ""
        department = str(row[5]).strip() if len(row) > 5 and row[5] else "General Physician"

        # Combined text for embedding — symptoms are the primary search target
        combined_text = f"Disease: {disease}. Symptoms: {symptoms}"

        records.append({
            "disease": disease,
            "symptoms": symptoms,
            "ayurvedic": ayurvedic,
            "allopathic": allopathic,
            "advice": advice,
            "department": department,
            "combined_text": combined_text,
        })
    return records


# ──────────────────────────────────────────────
# ChromaDB Setup & Indexing
# ──────────────────────────────────────────────
def build_vector_store(records: list[dict]):
    """Create ChromaDB collection and upsert disease embeddings."""
    # Wipe any previous database. ChromaDB stores have an on-disk format tied
    # to the library version; mixing versions (or a partial write) makes the
    # Rust-backed SQLite layer panic. The index is rebuilt every run anyway.
    if os.path.isdir(CHROMA_DIR):
        for entry in os.listdir(CHROMA_DIR):
            entry_path = os.path.join(CHROMA_DIR, entry)
            if os.path.isdir(entry_path):
                shutil.rmtree(entry_path, ignore_errors=True)
            else:
                os.remove(entry_path)

    client = chromadb.PersistentClient(path=CHROMA_DIR)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    # Prepare data for upserting
    ids = []
    documents = []
    metadatas = []
    embeddings_list = []

    for idx, rec in enumerate(records):
        ids.append(f"disease_{idx}")
        documents.append(rec["combined_text"])
        metadatas.append({
            "disease": rec["disease"],
            "symptoms": rec["symptoms"],
            "ayurvedic": rec["ayurvedic"],
            "allopathic": rec["allopathic"],
            "advice": rec["advice"],
            "department": rec["department"],
        })

    # Batch encode all combined texts
    print("🔢 Generating embeddings ...")
    embeddings = embedder.encode(
        [r["combined_text"] for r in records],
        show_progress_bar=True,
        convert_to_numpy=True,
    )
    embeddings_list = embeddings.tolist()

    # Upsert into ChromaDB
    collection.upsert(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings_list,
    )
    print(f"✅ Indexed {len(records)} diseases into ChromaDB.")
    return client


def query_vector_store(client, query_text: str, top_k: int = TOP_K):
    """Retrieve top-k matching diseases from ChromaDB."""
    collection = client.get_collection(COLLECTION_NAME)

    # Encode query
    query_embedding = embedder.encode(query_text, convert_to_numpy=True).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["metadatas", "distances", "documents"],
    )
    return results


# ──────────────────────────────────────────────
# Intelligent Input Validation
# ──────────────────────────────────────────────
def validate_medical_input(user_message: str) -> str | None:
    """
    Validate user input for medically impossible or nonsensical claims.
    Returns an error message string if invalid, or None if the input is okay.
    """
    msg = user_message.lower()

    # ── 1. Unrealistic fever/temperature ──
    fever_patterns = [
        r'(\d+)\s*(?:degree|°|deg)\s*(?:fever|temperature|temp|f|c|fahrenheit|celsius)?',
        r'fever\s*(?:of\s*)?(?:is\s*)?(?:around\s*)?(\d+)',
        r'temperature\s*(?:of\s*)?(?:is\s*)?(?:around\s*)?(\d+)',
        r'(\d+)\s*(?:degree|°)\s*(?:fever)',
    ]
    for pattern in fever_patterns:
        match = re.search(pattern, msg)
        if match:
            temp_val = float(match.group(1))
            # Fahrenheit range
            if temp_val > 115:
                return (
                    f"⚠️ A body temperature of {int(temp_val)}° is not medically possible "
                    f"for a living person. The highest recorded human body temperature is "
                    f"approximately 115°F (46.1°C). Temperatures above 108°F (42.2°C) are "
                    f"almost always fatal.\n\n"
                    f"Please double-check your temperature reading and try again with "
                    f"an accurate value. Normal body temperature is around 98.6°F (37°C)."
                )
            # Unrealistically low (below 80°F / 26.7°C alive is extremely rare)
            if 0 < temp_val < 70:
                return (
                    f"⚠️ A body temperature of {int(temp_val)}° is extremely unlikely. "
                    f"Human body temperature below 82°F (27.8°C) is life-threatening and "
                    f"rarely survivable.\n\n"
                    f"Please check your thermometer and provide an accurate reading. "
                    f"Normal body temperature is around 98.6°F (37°C)."
                )

    # ── 2. Unrealistic heart rate / pulse ──
    hr_patterns = [
        r'(?:heart\s*rate|pulse|bpm|heartbeat)\s*(?:of\s*)?(?:is\s*)?(?:around\s*)?(\d+)',
        r'(\d+)\s*(?:bpm|beats\s*per\s*minute)',
    ]
    for pattern in hr_patterns:
        match = re.search(pattern, msg)
        if match:
            hr_val = int(match.group(1))
            if hr_val > 300:
                return (
                    f"⚠️ A heart rate of {hr_val} BPM is not physiologically possible. "
                    f"The maximum recorded heart rate in humans rarely exceeds 250-300 BPM "
                    f"even during severe arrhythmias.\n\n"
                    f"Please verify your reading. Normal resting heart rate is 60-100 BPM."
                )
            if hr_val < 10 and hr_val > 0:
                return (
                    f"⚠️ A heart rate of {hr_val} BPM is not compatible with life. "
                    f"Anything below 20 BPM is extremely dangerous.\n\n"
                    f"Please verify your reading. Normal resting heart rate is 60-100 BPM."
                )

    # ── 3. Unrealistic blood pressure ──
    bp_pattern = r'(?:bp|blood\s*pressure)\s*(?:of\s*)?(?:is\s*)?(\d+)\s*/\s*(\d+)'
    bp_match = re.search(bp_pattern, msg)
    if bp_match:
        systolic = int(bp_match.group(1))
        diastolic = int(bp_match.group(2))
        if systolic > 350 or diastolic > 250:
            return (
                f"⚠️ A blood pressure of {systolic}/{diastolic} mmHg is not medically "
                f"realistic. The highest recorded blood pressure in medical literature "
                f"is around 300/200 mmHg.\n\n"
                f"Please verify your reading. Normal blood pressure is around 120/80 mmHg."
            )
        if systolic < diastolic:
            return (
                f"⚠️ A blood pressure reading where systolic ({systolic}) is lower than "
                f"diastolic ({diastolic}) is not possible. The systolic value (top number) "
                f"should always be higher than the diastolic value (bottom number).\n\n"
                f"Normal blood pressure is around 120/80 mmHg."
            )

    # ── 4. Unrealistic blood sugar ──
    sugar_patterns = [
        r'(?:blood\s*sugar|glucose)\s*(?:level)?\s*(?:of\s*)?(?:is\s*)?(\d+)',
        r'(?:sugar)\s*(?:level)?\s*(?:of\s*)?(?:is\s*)?(\d+)',
    ]
    for pattern in sugar_patterns:
        match = re.search(pattern, msg)
        if match:
            sugar = int(match.group(1))
            if sugar > 1500:
                return (
                    f"⚠️ A blood sugar level of {sugar} mg/dL is beyond any recorded "
                    f"survivable range. Levels above 600 mg/dL constitute a medical "
                    f"emergency (diabetic coma).\n\n"
                    f"Please verify your reading. Normal fasting blood sugar is 70-100 mg/dL."
                )

    # ── 5. Unrealistic age claims ──
    age_patterns = [
        r'(?:i\s*am|age\s*(?:is)?|i\'m)\s*(\d+)\s*(?:years?\s*old|yrs?)',
        r'(\d+)\s*(?:years?\s*old|yrs?\s*old)',
    ]
    for pattern in age_patterns:
        match = re.search(pattern, msg)
        if match:
            age = int(match.group(1))
            if age > 150:
                return (
                    f"⚠️ An age of {age} years is not realistic. The oldest verified "
                    f"person lived to 122 years. Please provide your actual age for "
                    f"accurate medical guidance."
                )
            if age < 0:
                return "⚠️ Age cannot be negative. Please provide a valid age."

    # ── 6. Unrealistic weight ──
    weight_patterns = [
        r'(?:weight|weigh)\s*(?:is\s*)?(?:around\s*)?(\d+)\s*(?:kg|kilogram)',
        r'(\d+)\s*(?:kg|kilogram)\s*(?:weight)',
    ]
    for pattern in weight_patterns:
        match = re.search(pattern, msg)
        if match:
            weight = int(match.group(1))
            if weight > 700:
                return (
                    f"⚠️ A weight of {weight} kg is beyond any recorded human weight. "
                    f"The heaviest person ever recorded weighed approximately 635 kg.\n\n"
                    f"Please provide an accurate weight for proper medical guidance."
                )

    # ── 7. Contradictory symptoms ──
    if 'no symptoms' in msg and ('diagnos' in msg or 'disease' in msg or 'what do i have' in msg):
        return (
            "You've mentioned that you have no symptoms. Without any symptoms, "
            "it's not possible to suggest a diagnosis.\n\n"
            "If you're feeling well, that's great! For routine health check-ups, "
            "please visit a General Physician."
        )

    # ── 8. Non-medical or greetings ──
    greetings = ['hello', 'hi', 'hey', 'good morning', 'good evening', 'good afternoon', 'howdy', 'greetings']
    if msg.strip().rstrip('!. ') in greetings:
        return (
            "Hello! 👋 I'm your Medical Support assistant. \n\n"
            "Please describe your symptoms or ask a medical question, and I'll "
            "do my best to help you.\n\n"
            "For example: \"I have a headache, fever, and sore throat\""
        )

    # ── 9. Thank you / goodbye ──
    thanks = ['thank you', 'thanks', 'thank u', 'thx', 'bye', 'goodbye', 'good bye', 'see you']
    if msg.strip().rstrip('!. ') in thanks:
        return (
            "You're welcome! 😊 Take care of your health.\n\n"
            "Remember, always consult a healthcare professional for serious "
            "medical concerns. Feel free to ask if you have more questions!"
        )

    return None  # Input is valid


# ──────────────────────────────────────────────
# Confidence Threshold
# ──────────────────────────────────────────────
CONFIDENCE_THRESHOLD = 1.25  # Max cosine distance; above this = low confidence


# ──────────────────────────────────────────────
# Response Formatter (Rule-based)
# ──────────────────────────────────────────────
def format_response(results: dict) -> str:
    """Format RAG retrieval results into a structured medical response."""
    if not results or not results.get("metadatas") or not results["metadatas"][0]:
        return (
            "I'm sorry, I couldn't find a matching condition based on the symptoms "
            "you described. Please provide more details or consult a healthcare professional."
        )

    # Check confidence via distance score
    distances = results.get("distances", [[]])[0]
    if distances and distances[0] > CONFIDENCE_THRESHOLD:
        return (
            "🤔 I wasn't able to confidently match your description to any known condition "
            "in my database. This could mean:\n\n"
            "- The symptoms described are too vague or general\n"
            "- The condition may not be in my current database\n"
            "- The input may not describe medical symptoms\n\n"
            "Please try rephrasing with specific symptoms (e.g., \"fever, headache, "
            "body aches, sore throat\") or consult a healthcare professional directly."
        )

    top_match = results["metadatas"][0][0]
    disease = top_match.get("disease", "Unknown")
    symptoms = top_match.get("symptoms", "")
    ayurvedic_raw = top_match.get("ayurvedic", "")
    allopathic_raw = top_match.get("allopathic", "")
    advice = top_match.get("advice", "")
    department = top_match.get("department", "General Physician")

    # Format Ayurvedic medicines
    ayurvedic_lines = []
    for med in ayurvedic_raw.split(";"):
        med = med.strip()
        if med:
            ayurvedic_lines.append(f"- {med}")
    ayurvedic_formatted = "\n".join(ayurvedic_lines) if ayurvedic_lines else "- No specific Ayurvedic medicines found."

    # Format Allopathic medicines
    allopathic_lines = []
    for med in allopathic_raw.split(";"):
        med = med.strip()
        if med:
            allopathic_lines.append(f"- {med}")
    allopathic_formatted = "\n".join(allopathic_lines) if allopathic_lines else "- No specific Allopathic medicines found."

    # Also gather secondary matches for mention
    other_matches = []
    if len(results["metadatas"][0]) > 1:
        for m in results["metadatas"][0][1:]:
            other_matches.append(m.get("disease", ""))

    other_conditions_text = ""
    if other_matches:
        other_conditions_text = (
            f"\n\n📌 Other possible conditions to consider: {', '.join(other_matches)}."
        )

    response = (
        f"1. Based on the symptoms you've described, it appears that you may be "
        f"suffering from **{disease}**.\n\n"
        f"2. Ayurvedic Medicines:\n{ayurvedic_formatted}\n\n"
        f"3. Allopathic Medicines:\n{allopathic_formatted}\n\n"
        f"4. {advice}"
        f"{other_conditions_text}\n\n"
        f"5. 🏥 Recommended Department: **{department}**\n\n"
        f"6. Advice: It's crucial that you consult a healthcare professional before "
        f"starting any medication or treatment regimen. They will be able to provide "
        f"you with the most suitable course of action based on your specific condition."
    )

    return response


# ──────────────────────────────────────────────
# Initialize RAG Pipeline
# ──────────────────────────────────────────────
print("📂 Loading dataset ...")
records = load_dataset(DATASET_PATH)
print(f"   Found {len(records)} disease records.")
chroma_client = build_vector_store(records)
print("🚀 RAG pipeline ready!\n")

# ──────────────────────────────────────────────
# Flask Routes
# ──────────────────────────────────────────────
@app.route("/")
def index():
    """Serve the frontend."""
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """Handle chat messages via RAG pipeline."""
    try:
        data = request.get_json(force=True)
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"error": "Empty message."}), 400

        # Validate input for impossible/unrealistic claims
        validation_error = validate_medical_input(user_message)
        if validation_error:
            return jsonify({
                "response": validation_error,
                "status": "ok",
                "device": device,
                "timestamp": datetime.now().strftime("%I:%M %p"),
            })

        # Query vector store
        results = query_vector_store(chroma_client, user_message, top_k=TOP_K)

        # Format response
        bot_response = format_response(results)

        return jsonify({
            "response": bot_response,
            "status": "ok",
            "device": device,
            "timestamp": datetime.now().strftime("%I:%M %p"),
        })

    except Exception as e:
        print(f"❌ Error in /chat: {e}")
        return jsonify({
            "error": "An internal error occurred. Please try again.",
            "details": str(e),
        }), 500


@app.route("/health", methods=["GET"])
def health():
    """Health-check endpoint."""
    return jsonify({
        "status": "ok",
        "device": device,
        "model": MODEL_NAME,
        "diseases_loaded": len(records),
    })


# ──────────────────────────────────────────────
# Run
# ──────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5001)
