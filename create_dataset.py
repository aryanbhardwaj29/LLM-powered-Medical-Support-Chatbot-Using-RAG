"""
Generate the 'Final Year Diseases Dataset.xlsx' with comprehensive medical data.
Run this once to create the dataset used by the RAG pipeline.
"""

import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Diseases"

headers = [
    "Disease",
    "Symptoms",
    "Ayurvedic Medicines",
    "Allopathic Medicines",
    "Advice",
    "Department"
]
ws.append(headers)

data = [
    [
        "Common Cold",
        "runny nose, sneezing, sore throat, mild fever, cough, body aches, nasal congestion",
        "Tulsi tea (₹30 Rs) - Boosts immunity and relieves congestion; Sitopaladi Churna (₹80 Rs) - Relieves cough and cold symptoms; Ginger honey mix (₹40 Rs) - Soothes sore throat",
        "Paracetamol (₹15 Rs) - Reduces fever and body aches; Cetirizine (₹20 Rs) - Relieves sneezing and runny nose",
        "Stay hydrated with warm fluids. Rest adequately. Avoid cold foods and drinks. Steam inhalation helps relieve congestion.",
        "General Physician / ENT (Otorhinolaryngology)"
    ],
    [
        "Influenza (Flu)",
        "high fever, severe body aches, fatigue, headache, chills, dry cough, sore throat, muscle pain",
        "Giloy Kadha (₹60 Rs) - Boosts immunity and reduces fever; Ashwagandha (₹120 Rs) - Reduces fatigue and boosts energy; Tulsi drops (₹50 Rs) - Natural antiviral",
        "Oseltamivir (₹200 Rs) - Antiviral for flu; Ibuprofen (₹25 Rs) - Reduces fever and pain",
        "Complete bed rest is essential. Drink plenty of warm fluids. Avoid contact with others to prevent spreading. Consult a doctor if symptoms persist beyond 5 days.",
        "General Physician / Internal Medicine"
    ],
    [
        "Migraine",
        "severe headache on one side, nausea, vomiting, sensitivity to light, sensitivity to sound, visual aura, throbbing pain",
        "Brahmi (₹90 Rs) - Calms the nervous system; Shankhpushpi (₹70 Rs) - Reduces stress-related headaches; Peppermint oil (₹60 Rs) - Topical relief for headache",
        "Sumatriptan (₹150 Rs) - Migraine-specific pain relief; Propranolol (₹40 Rs) - Preventive medication",
        "Identify and avoid triggers like bright lights, strong smells, and certain foods. Maintain a regular sleep schedule. Practice stress management techniques.",
        "Neurologist"
    ],
    [
        "Type 2 Diabetes",
        "frequent urination, excessive thirst, unexplained weight loss, fatigue, blurred vision, slow wound healing, tingling in hands and feet",
        "Karela juice (₹50 Rs) - Helps regulate blood sugar; Jamun seed powder (₹60 Rs) - Natural blood sugar reducer; Fenugreek seeds (₹30 Rs) - Improves insulin sensitivity",
        "Metformin (₹35 Rs) - First-line diabetes medication; Glimepiride (₹50 Rs) - Stimulates insulin production",
        "Monitor blood sugar levels regularly. Follow a low-carb, high-fiber diet. Exercise for at least 30 minutes daily. Regular check-ups with your doctor are crucial.",
        "Endocrinologist / Diabetologist"
    ],
    [
        "Hypertension (High Blood Pressure)",
        "headache, dizziness, blurred vision, chest pain, shortness of breath, nosebleeds, fatigue",
        "Arjuna bark powder (₹80 Rs) - Strengthens heart muscles; Ashwagandha (₹120 Rs) - Reduces stress and blood pressure; Garlic capsules (₹60 Rs) - Natural blood pressure reducer",
        "Amlodipine (₹30 Rs) - Calcium channel blocker; Losartan (₹45 Rs) - ARB for blood pressure control",
        "Reduce salt intake. Exercise regularly. Manage stress through yoga and meditation. Monitor blood pressure at home. Avoid smoking and excessive alcohol.",
        "Cardiologist / Internal Medicine"
    ],
    [
        "Gastritis",
        "stomach pain, nausea, bloating, indigestion, loss of appetite, vomiting, burning sensation in stomach, hiccups",
        "Avipattikar Churna (₹70 Rs) - Relieves acidity and indigestion; Yashtimadhu (₹80 Rs) - Soothes stomach lining; Amla powder (₹40 Rs) - Natural antacid",
        "Omeprazole (₹30 Rs) - Reduces stomach acid; Antacid syrup (₹50 Rs) - Quick relief from acidity",
        "Eat smaller, more frequent meals. Avoid spicy, fried, and acidic foods. Don't lie down immediately after eating. Reduce stress and avoid NSAIDs on empty stomach.",
        "Gastroenterologist"
    ],
    [
        "Asthma",
        "wheezing, shortness of breath, chest tightness, coughing especially at night, difficulty breathing during exercise, rapid breathing",
        "Vasaka (₹60 Rs) - Bronchodilator and expectorant; Haridra (Turmeric) (₹40 Rs) - Anti-inflammatory for airways; Kantakari (₹55 Rs) - Relieves bronchial congestion",
        "Salbutamol inhaler (₹120 Rs) - Quick relief bronchodilator; Budesonide inhaler (₹250 Rs) - Preventive corticosteroid",
        "Always carry your rescue inhaler. Avoid known triggers like dust, smoke, and allergens. Practice breathing exercises. Get regular check-ups and follow your action plan.",
        "Pulmonologist / Chest Physician"
    ],
    [
        "External Ear Infection",
        "itching in ear canal, redness, discomfort, drainage of clear fluid, ear pain, swelling, reduced hearing, tenderness",
        "Diluted Apple Cider Vinegar drops (Price varies depending on the concentration) - Restores ear pH; Garlic oil (₹40 Rs) - Natural antibacterial and anti-inflammatory; Neem oil drops (₹35 Rs) - Antiseptic",
        "Ciprofloxacin ear drops (₹60 Rs) - Antibiotic for infection; Hydrocortisone drops (₹45 Rs) - Reduces inflammation",
        "Keep ears dry. Avoid inserting objects into the ear canal. Use earplugs while swimming. Do not use earbuds during infection. Consult an ENT specialist if pain persists.",
        "ENT Specialist (Otorhinolaryngologist)"
    ],
    [
        "Ligament Injury",
        "pain, swelling, bruising around joints, limited ability to move, instability in the joint, popping sensation, stiffness",
        "Nirgundi oil massage (₹100 Rs) - Helps reduce swelling and pain; Ginger compress (₹100 Rs) - Strengthens ligaments and aids in recovery; Turmeric milk (₹30 Rs) - Natural anti-inflammatory",
        "Ibuprofen (₹55 Rs) - Reduces swelling and pain; Diclofenac gel (₹80 Rs) - Topical pain relief",
        "RICE protocol is recommended in both Ayurveda and Allopathy which stands for Rest, Ice, Compression, and Elevation. This can help manage your symptoms effectively. Consult a healthcare professional before starting any medication.",
        "Orthopedic Surgeon / Sports Medicine Specialist"
    ],
    [
        "Dengue Fever",
        "high fever, severe headache, pain behind eyes, joint pain, muscle pain, skin rash, fatigue, mild bleeding from nose or gums",
        "Papaya leaf extract (₹50 Rs) - Helps increase platelet count; Giloy juice (₹60 Rs) - Boosts immunity and reduces fever; Tulsi and black pepper tea (₹25 Rs) - Natural antipyretic",
        "Paracetamol (₹15 Rs) - For fever and pain (avoid aspirin); ORS sachets (₹20 Rs) - Prevents dehydration",
        "Stay hydrated with fluids, ORS, and coconut water. Monitor platelet count regularly. Avoid aspirin and ibuprofen. Use mosquito nets and repellents. Seek immediate medical help if bleeding occurs.",
        "General Physician / Infectious Disease Specialist"
    ],
    [
        "Urinary Tract Infection (UTI)",
        "burning sensation during urination, frequent urge to urinate, cloudy urine, strong-smelling urine, pelvic pain, lower abdominal discomfort",
        "Punarnava (₹70 Rs) - Natural diuretic and anti-inflammatory; Gokshura (₹80 Rs) - Supports urinary tract health; Coriander seed water (₹20 Rs) - Cooling and soothing",
        "Nitrofurantoin (₹50 Rs) - Antibiotic for UTI; Ciprofloxacin (₹40 Rs) - Broad-spectrum antibiotic",
        "Drink plenty of water (8-10 glasses daily). Urinate frequently, don't hold it. Maintain good hygiene. Avoid irritants like caffeine and alcohol. Consult a doctor for recurring UTIs.",
        "Urologist / Nephrologist"
    ],
    [
        "Conjunctivitis (Pink Eye)",
        "redness in eye, itching, tearing, discharge from eye, swollen eyelids, sensitivity to light, gritty feeling in eyes",
        "Rose water drops (₹30 Rs) - Soothes and cleanses eyes; Triphala eye wash (₹50 Rs) - Natural antiseptic; Neem water compress (₹25 Rs) - Reduces infection",
        "Moxifloxacin eye drops (₹80 Rs) - Antibiotic drops; Olopatadine eye drops (₹120 Rs) - For allergic conjunctivitis",
        "Wash hands frequently. Avoid touching or rubbing eyes. Don't share towels or pillows. Use cold compress for relief. Replace eye makeup after infection clears.",
        "Ophthalmologist (Eye Specialist)"
    ],
    [
        "Anemia",
        "fatigue, weakness, pale skin, shortness of breath, dizziness, cold hands and feet, headache, fast heartbeat",
        "Loha Bhasma (₹100 Rs) - Iron supplement in Ayurveda; Draksha (Grapes) (₹80 Rs) - Natural iron booster; Punarnava Mandur (₹90 Rs) - Treats iron deficiency anemia",
        "Ferrous sulfate (₹25 Rs) - Iron supplement; Folic acid (₹15 Rs) - Supports red blood cell production",
        "Eat iron-rich foods like spinach, lentils, and red meat. Pair iron foods with vitamin C for better absorption. Avoid tea/coffee with meals. Get regular blood tests.",
        "Hematologist / General Physician"
    ],
    [
        "Arthritis",
        "joint pain, stiffness, swelling in joints, reduced range of motion, joint redness, morning stiffness, joint warmth",
        "Shallaki (Boswellia) (₹110 Rs) - Anti-inflammatory for joints; Guggulu (₹90 Rs) - Reduces joint swelling; Mahanarayan oil (₹130 Rs) - Joint massage oil",
        "Methotrexate (₹80 Rs) - Disease-modifying drug; Naproxen (₹30 Rs) - Anti-inflammatory pain relief",
        "Stay physically active with low-impact exercises. Apply hot/cold therapy. Maintain a healthy weight. Practice gentle yoga. Consult a rheumatologist for proper management.",
        "Rheumatologist / Orthopedic Surgeon"
    ],
    [
        "Bronchitis",
        "persistent cough, mucus production, chest discomfort, fatigue, shortness of breath, mild fever, wheezing, sore throat",
        "Vasaka syrup (₹65 Rs) - Expectorant and bronchodilator; Mulethi (Licorice) (₹45 Rs) - Soothes throat and airways; Honey and turmeric paste (₹35 Rs) - Natural cough suppressant",
        "Ambroxol (₹40 Rs) - Mucolytic for cough; Azithromycin (₹80 Rs) - Antibiotic if bacterial",
        "Avoid smoking and secondhand smoke. Use a humidifier. Stay hydrated. Rest adequately. Seek medical attention if coughing blood or fever persists over a week.",
        "Pulmonologist / General Physician"
    ],
    [
        "Eczema (Dermatitis)",
        "dry skin, itching, red patches, scaly skin, cracked skin, oozing blisters, thickened skin, skin inflammation",
        "Neem oil (₹50 Rs) - Antibacterial and anti-itch; Kumkumadi oil (₹200 Rs) - Skin rejuvenation; Aloe vera gel (₹40 Rs) - Soothes and moisturizes skin",
        "Hydrocortisone cream (₹35 Rs) - Reduces inflammation; Cetirizine (₹20 Rs) - Reduces itching",
        "Moisturize skin regularly. Avoid harsh soaps and detergents. Wear soft, breathable fabrics. Identify and avoid triggers. Don't scratch affected areas.",
        "Dermatologist (Skin Specialist)"
    ],
    [
        "Kidney Stones",
        "severe pain in side and back, pain during urination, pink or red urine, nausea, vomiting, frequent urination, foul-smelling urine",
        "Varuna (₹85 Rs) - Dissolves kidney stones; Pashanbhed (₹70 Rs) - Stone-breaking herb; Kulthi dal water (₹30 Rs) - Traditional stone dissolving remedy",
        "Tamsulosin (₹45 Rs) - Helps pass stones; Diclofenac (₹25 Rs) - Pain management",
        "Drink 3-4 liters of water daily. Reduce salt and protein intake. Avoid oxalate-rich foods if calcium oxalate stones. Get regular ultrasound check-ups.",
        "Urologist / Nephrologist"
    ],
    [
        "Sinusitis",
        "facial pain, nasal congestion, thick nasal discharge, reduced sense of smell, headache, pressure around eyes, cough, postnasal drip",
        "Nasya oil (₹60 Rs) - Nasal drops for congestion; Haridra (Turmeric) (₹40 Rs) - Anti-inflammatory; Eucalyptus steam (₹30 Rs) - Clears sinuses",
        "Amoxicillin (₹50 Rs) - Antibiotic for bacterial sinusitis; Fluticasone nasal spray (₹150 Rs) - Reduces nasal inflammation",
        "Use saline nasal irrigation. Apply warm compresses on face. Stay hydrated. Use a humidifier. Avoid allergens and pollutants. Consult ENT if symptoms persist over 10 days.",
        "ENT Specialist (Otorhinolaryngologist)"
    ],
    [
        "Thyroid Disorder (Hypothyroidism)",
        "fatigue, weight gain, cold sensitivity, dry skin, constipation, hair loss, depression, muscle weakness, puffy face",
        "Kanchanar Guggulu (₹100 Rs) - Thyroid function support; Ashwagandha (₹120 Rs) - Balances thyroid hormones; Shilajit (₹150 Rs) - Boosts metabolism",
        "Levothyroxine (₹30 Rs) - Thyroid hormone replacement; Regular TSH monitoring required",
        "Take medication on empty stomach in the morning. Avoid soy and calcium supplements near medication time. Exercise regularly. Get thyroid levels checked every 6 months.",
        "Endocrinologist"
    ],
    [
        "Malaria",
        "high fever with chills, sweating, headache, nausea, vomiting, muscle pain, fatigue, enlarged spleen",
        "Sudarshan Churna (₹80 Rs) - Traditional antimalarial; Neem leaf extract (₹45 Rs) - Antipyretic and antimalarial; Giloy Sat (₹70 Rs) - Boosts immunity and reduces fever",
        "Chloroquine (₹30 Rs) - Antimalarial drug; Artemisinin-based therapy (₹120 Rs) - For resistant malaria",
        "Complete the full course of antimalarial medication. Use mosquito nets and repellents. Eliminate standing water near home. Seek immediate treatment for high fever with chills.",
        "General Physician / Infectious Disease Specialist"
    ],
    [
        "Peptic Ulcer",
        "burning stomach pain, bloating, heartburn, nausea, vomiting, dark stools, weight loss, pain worse when stomach is empty",
        "Shatavari (₹90 Rs) - Heals and protects stomach lining; Yashtimadhu (₹80 Rs) - Natural antacid and ulcer healer; Amalaki (₹50 Rs) - Reduces stomach acid",
        "Pantoprazole (₹40 Rs) - Proton pump inhibitor; Sucralfate (₹60 Rs) - Protects ulcer surface",
        "Avoid spicy, acidic, and fried foods. Don't take NSAIDs. Quit smoking and alcohol. Eat smaller, frequent meals. Get tested for H. pylori infection.",
        "Gastroenterologist"
    ],
    [
        "Psoriasis",
        "red patches with silvery scales, dry cracked skin, itching, burning sensation, thickened nails, stiff joints, skin flaking",
        "Panchatikta Ghrita Guggulu (₹130 Rs) - Blood purifier for skin; Bakuchi oil (₹70 Rs) - Topical psoriasis treatment; Neem capsules (₹60 Rs) - Blood purifier",
        "Methotrexate (₹80 Rs) - Immunosuppressant; Calcipotriol ointment (₹120 Rs) - Vitamin D analog for skin",
        "Moisturize skin daily. Avoid triggers like stress and skin injuries. Get moderate sun exposure. Avoid alcohol. Follow prescribed treatment consistently.",
        "Dermatologist (Skin Specialist)"
    ],
    [
        "Pneumonia",
        "cough with phlegm, high fever, chest pain while breathing, shortness of breath, fatigue, chills, sweating, confusion in elderly",
        "Sitopaladi Churna (₹80 Rs) - Relieves cough and congestion; Kantakari (₹55 Rs) - Clears chest congestion; Tulsi Ark (₹40 Rs) - Natural antimicrobial",
        "Amoxicillin-Clavulanate (₹90 Rs) - Antibiotic combination; Azithromycin (₹80 Rs) - Macrolide antibiotic",
        "Complete the full antibiotic course. Rest and stay hydrated. Use a humidifier. Practice deep breathing exercises. Get pneumonia vaccine if at risk. Seek emergency care if breathing becomes very difficult.",
        "Pulmonologist / General Physician"
    ],
    [
        "Insomnia",
        "difficulty falling asleep, waking up during night, waking up too early, daytime fatigue, irritability, difficulty concentrating, anxiety about sleep",
        "Ashwagandha (₹120 Rs) - Promotes relaxation and sleep; Jatamansi (₹90 Rs) - Natural sedative; Brahmi (₹90 Rs) - Calms the mind",
        "Melatonin (₹80 Rs) - Sleep hormone supplement; Zolpidem (₹60 Rs) - Short-term sleep aid (prescription only)",
        "Maintain a consistent sleep schedule. Avoid screens 1 hour before bed. Limit caffeine after 2 PM. Create a dark, cool sleeping environment. Practice relaxation techniques before bed.",
        "Psychiatrist / Sleep Medicine Specialist"
    ],
    [
        "Allergic Rhinitis",
        "sneezing, runny nose, itchy nose, nasal congestion, watery eyes, itchy throat, postnasal drip, reduced sense of smell",
        "Haridra Khand (₹70 Rs) - Anti-allergic; Tulsi drops (₹50 Rs) - Immune modulator; Sitopladi with honey (₹60 Rs) - Reduces nasal symptoms",
        "Fexofenadine (₹30 Rs) - Non-drowsy antihistamine; Montelukast (₹40 Rs) - Leukotriene inhibitor",
        "Identify and avoid allergens. Use air purifiers at home. Wash bedding in hot water weekly. Shower after outdoor activities. Keep windows closed during high pollen seasons.",
        "Allergist / Immunologist / ENT Specialist"
    ],
    [
        "Irritable Bowel Syndrome (IBS)",
        "abdominal pain, bloating, gas, diarrhea, constipation, mucus in stool, cramping, alternating bowel habits",
        "Kutajarishta (₹80 Rs) - Controls diarrhea; Hingvastak Churna (₹60 Rs) - Reduces bloating and gas; Triphala (₹50 Rs) - Regulates bowel movements",
        "Mebeverine (₹45 Rs) - Antispasmodic; Rifaximin (₹200 Rs) - For IBS with diarrhea",
        "Follow a low-FODMAP diet. Eat regular meals and chew food well. Exercise regularly. Manage stress through yoga and meditation. Keep a food diary to identify triggers.",
        "Gastroenterologist"
    ],
    [
        "Chickenpox",
        "itchy rash with fluid-filled blisters, fever, fatigue, headache, loss of appetite, body aches, blisters spreading across body",
        "Neem leaf bath (₹30 Rs) - Antiseptic and anti-itch; Manjistha (₹80 Rs) - Blood purifier; Sandalwood paste (₹60 Rs) - Cooling and soothing for skin",
        "Acyclovir (₹120 Rs) - Antiviral medication; Calamine lotion (₹50 Rs) - Relieves itching",
        "Keep nails trimmed to avoid scratching. Take lukewarm baths with neem. Stay isolated until blisters crust over. Stay hydrated. Consult doctor for adults and immunocompromised patients.",
        "General Physician / Dermatologist"
    ],
    [
        "Sciatica",
        "lower back pain radiating to leg, sharp shooting pain, numbness in leg, tingling sensation, weakness in leg, pain worse when sitting, difficulty standing",
        "Dashmool Kwath (₹90 Rs) - Anti-inflammatory decoction; Bala oil massage (₹120 Rs) - Nerve strengthening; Guggulu (₹90 Rs) - Reduces nerve inflammation",
        "Pregabalin (₹70 Rs) - Nerve pain medication; Diclofenac (₹25 Rs) - Anti-inflammatory",
        "Practice gentle stretching exercises. Avoid prolonged sitting. Use proper posture. Apply hot/cold packs. Sleep on a firm mattress. Consider physiotherapy for chronic cases.",
        "Orthopedic Surgeon / Neurologist / Physiotherapist"
    ],
    [
        "Jaundice",
        "yellowing of skin, yellowing of eyes, dark urine, pale stools, fatigue, abdominal pain, nausea, loss of appetite, itching",
        "Kutki (₹100 Rs) - Liver protective herb; Bhumi Amla (₹70 Rs) - Supports liver regeneration; Sugarcane juice (₹20 Rs) - Traditional liver tonic",
        "Ursodeoxycholic acid (₹80 Rs) - For liver support; Liver function monitoring required",
        "Rest adequately. Eat a high-carb, low-fat diet. Avoid alcohol completely. Stay hydrated. Get liver function tests done regularly. Consult a hepatologist for persistent symptoms.",
        "Hepatologist / Gastroenterologist"
    ],
    [
        "Acne",
        "pimples, blackheads, whiteheads, oily skin, skin redness, painful bumps under skin, scarring, skin inflammation on face",
        "Kumkumadi oil (₹200 Rs) - Skin brightening and anti-acne; Neem face wash (₹60 Rs) - Antibacterial; Turmeric and sandalwood paste (₹40 Rs) - Reduces inflammation",
        "Benzoyl peroxide gel (₹80 Rs) - Kills acne bacteria; Adapalene gel (₹120 Rs) - Retinoid for acne",
        "Wash face twice daily with gentle cleanser. Don't pick or squeeze pimples. Use non-comedogenic products. Stay hydrated and eat balanced diet. Change pillowcases regularly.",
        "Dermatologist (Skin Specialist)"
    ],
]

for row in data:
    ws.append(row)

# Adjust column widths
ws.column_dimensions['A'].width = 30
ws.column_dimensions['B'].width = 60
ws.column_dimensions['C'].width = 80
ws.column_dimensions['D'].width = 60
ws.column_dimensions['E'].width = 80
ws.column_dimensions['F'].width = 40

wb.save("Final Year Diseases Dataset.xlsx")
print("✅ Dataset created successfully: Final Year Diseases Dataset.xlsx")
print(f"   Total diseases: {len(data)}")
print("   Columns: Disease, Symptoms, Ayurvedic Medicines, Allopathic Medicines, Advice, Department")
