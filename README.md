# AyurDiag — AI-Powered Ayurvedic & Medical Assistant

A Retrieval-Augmented Generation (RAG) chatbot built with Flask, SentenceTransformers, and ChromaDB. Users describe their symptoms in plain language, and the assistant matches them against a database of **161 diseases** across 77 specialties — then returns the likely condition alongside both **Ayurvedic** and **Allopathic** medicine suggestions and the recommended medical department.

## Overview

- User submits symptoms in natural language via a chat interface.
- Inputs are validated for impossible or nonsensical medical claims (unrealistic temperature, heart rate, blood pressure, blood sugar, age, weight, contradictory symptoms, etc.).
- The query is embedded with `all-MiniLM-L6-v2` and matched against a ChromaDB vector store of disease records using cosine similarity.
- A confidence threshold determines whether a diagnosis is shown or the assistant asks for more detail.
- Responses render as a structured "diagnosis card" in the frontend, showing the condition, medicines, advice, and department.

## Tech Stack

- Python 3.10+
- Flask
- sentence-transformers (`all-MiniLM-L6-v2`)
- ChromaDB (vector store, cosine distance)
- openpyxl (dataset loading)
- Vanilla HTML / CSS / JavaScript (with Web Speech API voice input)

## How to Run

1. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

2. (Optional) The dataset is already provided as `Final Year Diseases Dataset.xlsx`. To regenerate the base 30 diseases:

   ```
   python create_dataset.py
   ```

   To expand the dataset with 131 additional diseases (161 total) without duplicating any existing ones:

   ```
   python expand_dataset.py
   ```

3. Start the server:

   ```
   python app.py
   ```

4. Open http://127.0.0.1:5001 in your browser.

Note: the first run downloads the `all-MiniLM-L6-v2` embedding model and re-indexes the disease records into `chroma_db/`, so startup takes longer the first time.

## Project Structure

```
app.py                  Flask backend, RAG pipeline, input validation, response formatting
create_dataset.py       Generates the base diseases Excel dataset
expand_dataset.py       Expands the dataset with 131 additional diseases (deduplicates)
requirements.txt        Python dependencies
templates/index.html    Chat interface
static/style.css        Styling (diagnosis card, typing indicator, etc.)
static/script.js        Chat logic, rendering, voice input
Final Year Diseases Dataset.xlsx    Dataset (161 diseases)
chroma_db/              ChromaDB persistence (auto-generated, gitignored)
```

## Disclaimer

AyurDiag is an AI assistant, not a substitute for professional medical advice. Always consult a qualified healthcare provider for serious concerns.