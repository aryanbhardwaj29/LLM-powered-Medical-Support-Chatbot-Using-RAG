"""
Expand the 'Final Year Diseases Dataset.xlsx' with a large set of additional
diseases covering all major body systems. Safe to run repeatedly — existing
disease names are never duplicated.

Run:
    python expand_dataset.py
"""

import openpyxl

FILE = "Final Year Diseases Dataset.xlsx"

# Format: [Disease, Symptoms, Ayurvedic Medicines, Allopathic Medicines, Advice, Department]
EXPANSION = [
    # ─────────────────────────── Infectious diseases ───────────────────────────
    [
        "Typhoid Fever",
        "prolonged high fever, headache, weakness, fatigue, abdominal pain, constipation or diarrhea, loss of appetite, rose spots on chest, dry cough",
        "Sudarshan Churna (₹80 Rs) - Reduces fever and infection; Kumari (Aloe vera) (₹45 Rs) - Cools the system; Amalaki (₹50 Rs) - Boosts immunity",
        "Ceftriaxone (₹90 Rs) - Antibiotic for typhoid; Azithromycin (₹85 Rs) - Alternative antibiotic",
        "Drink boiled water and fluids. Rest completely. Eat soft, easily digestible food. Complete the full antibiotic course. Wash hands regularly.",
        "General Physician / Infectious Disease Specialist"
    ],
    [
        "Measles",
        "high fever, cough, runny nose, red watery eyes, white spots inside mouth, red rash spreading from face down the body, fatigue",
        "Tulsi drops (₹50 Rs) - Antiviral and immune support; Trikatu churna (₹40 Rs) - Clears congestion; Neem bath (₹30 Rs) - Soothes skin rash",
        "Paracetamol (₹15 Rs) - Reduces fever; Vitamin A supplements (₹20 Rs) - Reduces complications",
        "Rest and isolate to prevent spread. Offer plenty of fluids. Use a cool-mist humidifier. Vaccination (MMR) is the best prevention.",
        "General Physician / Pediatrician"
    ],
    [
        "Mumps",
        "swollen painful salivary glands, fever, headache, earache on chewing, fatigue, jaw pain, loss of appetite, muscle aches",
        "Dashamoola Kwath (₹90 Rs) - Reduces gland swelling; Honey and ginger (₹40 Rs) - Soothes throat; Guduchi (₹60 Rs) - Antiviral support",
        "Paracetamol (₹15 Rs) - Pain and fever relief; Warm compresses along with analgesics",
        "Rest and isolate until swelling subsides. Apply warm or cold compresses to the swollen area. Drink fluids and eat soft foods. Avoid acidic foods.",
        "General Physician / Pediatrician"
    ],
    [
        "Rubella (German Measles)",
        "low-grade fever, pink rash starting on face and spreading down, mild headache, runny nose, swollen tender lymph nodes, joint pain, red eyes",
        "Neem capsules (₹60 Rs) - Blood purifier; Manjistha (₹80 Rs) - Skin detox; Giloy (₹60 Rs) - Immune booster",
        "Paracetamol (₹15 Rs) - For fever and aches; Rest and supportive care",
        "Rest and hydrate well. Avoid contact with pregnant women. Vaccination (MMR) prevents infection. Isolate for about a week after rash appears.",
        "General Physician"
    ],
    [
        "Whooping Cough (Pertussis)",
        "severe coughing fits, whooping sound on breathing in, cough ending in vomiting, runny nose, low fever, fatigue, breathlessness",
        "Sitopaladi Churna (₹80 Rs) - Relieves cough; Vasaka syrup (₹65 Rs) - Calms bronchial spasm; Honey and black pepper (₹30 Rs) - Soothes throat",
        "Azithromycin (₹80 Rs) - Antibiotic for pertussis; Cough syrup to relieve symptoms",
        "Finish the prescribed antibiotics. Use a humidifier. Eat small frequent meals. Get vaccinated (DPT/Tdap) for you and children.",
        "General Physician / Pediatrician"
    ],
    [
        "Tetanus",
        "stiff jaw muscles, painful muscle spasms, stiffness in neck and abdomen, difficulty swallowing, fever, sweating, rapid heart rate",
        "Emergency care needed; post-exposure Ayurvedic tonic - Shatavari (₹90 Rs) - Nerve tonic; Ashwagandha (₹120 Rs) - Muscle recovery",
        "Tetanus toxoid vaccine (₹150 Rs) - Protection; Tetanus immunoglobulin (₹400 Rs) - Immediate neutralization; Diazepam (₹30 Rs) - Muscle spasms",
        "Seek emergency medical care immediately. Complete the tetanus vaccination series. Clean wounds thoroughly with soap and water.",
        "Emergency Medicine / General Physician"
    ],
    [
        "Scarlet Fever",
        "sore throat, red rash like sandpaper, high fever, flushed face with pale ring around mouth, strawberry tongue, red lines in skin folds",
        "Tulsi tea (₹30 Rs) - Antipyretic; Haridra (Turmeric) (₹40 Rs) - Anti-inflammatory; Gargling with Triphala water (₹20 Rs) - Soothes throat",
        "Amoxicillin (₹50 Rs) - Antibiotic; Ibuprofen (₹25 Rs) - Reduces fever and pain",
        "Complete the full antibiotic course. Gargle with warm salt water. Stay hydrated. Rest and isolate to avoid spreading.",
        "General Physician / Pediatrician"
    ],
    [
        "Leptospirosis",
        "high fever, severe headache, muscle aches especially calves, chills, red eyes, abdominal pain, nausea, vomiting, jaundice",
        "Giloy juice (₹60 Rs) - Immune support; Kutki (₹100 Rs) - Liver protection; Tulsi (₹50 Rs) - Antipyretic",
        "Doxycycline (₹70 Rs) - Antibiotic; Paracetamol (₹15 Rs) - Fever relief",
        "Complete antibiotics as prescribed. Drink safe boiled water. Avoid contact with contaminated water. Control rodents near home.",
        "General Physician / Infectious Disease Specialist"
    ],
    [
        "Hand, Foot and Mouth Disease",
        "fever, sore throat, painful red blisters on hands, blisters on feet, mouth ulcers, poor appetite, irritability, drooling in children",
        "Triphala mouth rinse (₹50 Rs) - Heals mouth ulcers; Neem bath (₹30 Rs) - Soothes blisters; Honey (₹40 Rs) - Soothes ulcers",
        "Paracetamol (₹15 Rs) - Fever and pain; Oral rehydration for fluid balance, soothing mouth gel",
        "Give cool, soft foods and fluids. Avoid spicy and acidic foods. Keep blisters clean. Ensure good hand hygiene.",
        "Pediatrician / General Physician"
    ],
    [
        "Viral Gastroenteritis (Stomach Flu)",
        "watery diarrhea, stomach cramps, nausea, vomiting, low-grade fever, headache, muscle aches, dehydration, bloating",
        "Kutajarishta (₹80 Rs) - Controls diarrhea; Pomegranate juice (₹50 Rs) - Astringent; Ginger and honey tea (₹30 Rs) - Settles the stomach",
        "ORS sachets (₹20 Rs) - Prevents dehydration; Zinc tablets (₹15 Rs) - Shortens illness; Antiemetic if needed",
        "Stay well hydrated with ORS and clear fluids. Eat bland foods (bananas, rice, toast). Wash hands frequently. Avoid dairy and fried food.",
        "General Physician / Gastroenterologist"
    ],
    [
        "Food Poisoning",
        "nausea, vomiting, watery diarrhea, stomach cramps, fever, weakness, dehydration, loss of appetite, headache",
        "Ginger infusion (₹30 Rs) - Soothes the stomach; Pomegranate rind decoction (₹40 Rs) - Controls diarrhea; Ajwain water (₹25 Rs) - Digestion",
        "ORS sachets (₹20 Rs) - Rehydration; Anti-diarrheal only if prescribed; Antibiotics only for bacterial causes",
        "Rest your stomach with small sips of water. Rehydrate with ORS. Avoid solid food until vomiting stops. Seek care if blood in stool or high fever.",
        "General Physician / Gastroenterologist"
    ],
    [
        "Tuberculosis (TB)",
        "persistent cough with blood in sputum, unexplained weight loss, night sweats, low-grade evening fever, chest pain, fatigue, loss of appetite",
        "Vasa (₹60 Rs) - Lung tonic; Sitopaladi churna (₹80 Rs) - Respiratory support; Ashwagandha (₹120 Rs) - Restores strength",
        "Isoniazid + Rifampicin combination (₹120 Rs) - Anti-TB therapy (DOTS); Pyrazinamide and Ethambutol per regimen",
        "Complete the full 6-month DOTS treatment. Maintain good nutrition. Cover your mouth and use masks. Regular sputum and follow-up tests.",
        "Pulmonologist / TB Specialist"
    ],
    [
        "Hepatitis A",
        "jaundice, dark urine, pale stools, fatigue, nausea, vomiting, abdominal pain, fever, loss of appetite",
        "Kutki (₹100 Rs) - Liver protective; Bhumi Amla (₹70 Rs) - Liver regeneration; Sugarcane juice (₹20 Rs) - Liver tonic",
        "Supportive care; fluids and rest; test liver function; vaccination for prevention",
        "Rest completely and eat a light diet. Avoid alcohol and fatty foods. Wash hands and drink boiled water. Vaccination prevents infection.",
        "Hepatologist / Gastroenterologist"
    ],
    [
        "Hepatitis B",
        "jaundice, fatigue, dark urine, abdominal pain, nausea, loss of appetite, joint pain, fever, easy bruising",
        "Kutki (₹100 Rs) - Hepatoprotective; Guduchi (₹60 Rs) - Immune modulator; Punarnava (₹70 Rs) - Supports liver",
        "Tenofovir (₹150 Rs) - Antiviral; Entecavir (₹200 Rs) - Alternative; Hepatitis B vaccine for prevention",
        "Complete antiviral therapy under specialist guidance. Avoid alcohol completely. Use protection during sex. Never share needles. Get vaccinated.",
        "Hepatologist / Gastroenterologist"
    ],
    [
        "Shingles (Herpes Zoster)",
        "painful burning blistering rash on one side, tingling before rash, fever, headache, chills, fatigue, sensitivity to touch",
        "Neem paste (₹45 Rs) - Antiviral; Manjistha (₹80 Rs) - Blood purifier; Guduchi (₹60 Rs) - Immune support",
        "Acyclovir (₹120 Rs) - Antiviral; Gabapentin (₹70 Rs) - Nerve pain; Calamine lotion (₹50 Rs) - Itch relief",
        "Start antivirals within 72 hours of rash. Keep rash clean and dry. Use cool compresses. Get the shingles vaccine if over 50.",
        "Dermatologist / General Physician"
    ],
    [
        "Ringworm (Tinea)",
        "circular itchy red patches, raised scaly border, clearing center, itching, peeling skin, broken blisters, spread to other areas",
        "Neem leaf paste (₹35 Rs) - Antifungal; Turmeric paste (₹40 Rs) - Anti-inflammatory; Garlic oil (₹40 Rs) - Antifungal",
        "Clotrimazole cream (₹40 Rs) - Antifungal; Terbinafine (₹90 Rs) - Oral antifungal",
        "Apply antifungal cream for at least 2-4 weeks. Keep the skin dry. Wash clothes and towels in hot water. Avoid sharing personal items.",
        "Dermatologist"
    ],
    [
        "Scabies",
        "intense itching worse at night, thin burrow lines on skin, bumps and blisters, itching between fingers, rash on wrists and waist, sores from scratching",
        "Neem oil (₹50 Rs) - Kills mites; Turmeric and neem bath (₹30 Rs) - Soothes itching; Kutaja (₹70 Rs) - Antiparasitic",
        "Permethrin cream (₹60 Rs) - Kills scabies mites; Ivermectin (₹80 Rs) - Oral antiparasitic; antihistamine for itching",
        "Treat all household contacts at the same time. Wash bedding and clothes in hot water. Apply cream to the whole body. Vacuum furniture.",
        "Dermatologist"
    ],
    [
        "Cellulitis",
        "red swollen painful skin, warmth over the area, fever, chills, blisters, skin that looks dimpled, tenderness, red streaks",
        "Manjistha (₹80 Rs) - Blood purifier; Neem capsules (₹60 Rs) - Antibacterial; Turmeric milk (₹30 Rs) - Anti-inflammatory",
        "Cephalexin (₹60 Rs) - Antibiotic; Clindamycin (₹120 Rs) - If resistant; pain relievers",
        "Take antibiotics as prescribed and finish the course. Elevate the affected limb. Apply cool compresses. Watch for spreading redness.",
        "Dermatologist / General Physician"
    ],
    [
        "Chikungunya",
        "sudden high fever, severe joint pain and stiffness, rash, headache, muscle pain, fatigue, swelling in joints, nausea",
        "Giloy juice (₹60 Rs) - Reduces fever and joint pain; Dashamoola kwath (₹90 Rs) - Joint and muscle pain; Ashwagandha (₹120 Rs) - Recovery",
        "Paracetamol (₹15 Rs) - Fever and pain (avoid aspirin); adequate hydration",
        "Rest and hydrate well. Use mosquito repellents and nets. Apply warm compresses to stiff joints. Consult a doctor for persisting joint pain.",
        "General Physician / Infectious Disease Specialist"
    ],
    [
        "Rheumatic Fever",
        "fever, painful swollen joints, chest pain, heart murmur, tiredness, jerky uncontrollable movements, skin rash, nodules under skin",
        "Soothing cardiac tonics - Arjuna (₹80 Rs) - Heart support; Ashwagandha (₹120 Rs) - Anti-inflammatory; Guduchi (₹60 Rs) - Immunity",
        "Penicillin (₹40 Rs) - Treats streptococcal infection; Aspirin or other anti-inflammatory; steroids for severe cases",
        "Complete antibiotics to treat strep throat. Long-term penicillin prophylaxis needed. Bed rest during active phase. Regular heart check-ups.",
        "Cardiologist / General Physician"
    ],
    [
        "Meningitis",
        "sudden high fever, severe headache, stiff neck, nausea, vomiting, sensitivity to light, confusion, seizures, drowsiness",
        "Emergency care required; Ayurvedic supportive care after stabilization - Brahmi (₹90 Rs) - Nerve support",
        "Ceftriaxone (₹90 Rs) - IV antibiotic; Dexamethasone (₹30 Rs) - Reduces inflammation; fluids and supportive care",
        "Seek emergency medical care immediately. Complete the full antibiotic course. Rest in a quiet dark room. Vaccination prevents many causes.",
        "Emergency Medicine / Neurologist"
    ],
    [
        "Encephalitis",
        "fever, severe headache, confusion, seizures, stiff neck, sensitivity to light, drowsiness, irritability, muscle weakness",
        "Emergency care required; Brahmi (₹90 Rs) - Later nerve recovery; Ashwagandha (₹120 Rs) - Strength support",
        "Antiviral therapy (Acyclovir) (₹120 Rs); supportive care; anti-seizure medication; IV fluids",
        "Seek emergency care immediately. Hospital monitoring required. Ensure vaccination coverage in endemic areas. Mosquito control reduces risk.",
        "Emergency Medicine / Neurologist"
    ],
    [
        "HIV/AIDS",
        "fever, swollen lymph nodes, sore throat, fatigue, night sweats, unexplained weight loss, recurrent infections, skin rashes, mouth sores",
        "Ashwagandha (₹120 Rs) - Immune strength; Guduchi (₹60 Rs) - Immunity modulator; Tulsi (₹50 Rs) - Antimicrobial support",
        "Antiretroviral therapy (ART) (Integrated counselling); cotrimoxazole prophylaxis for opportunistic infections",
        "Start ART immediately and never miss doses. Regular CD4 and viral load tests. Safe practices prevent transmission. Eat a nutritious diet.",
        "Infectious Disease Specialist / Antiretroviral Therapy Center"
    ],

    # ─────────────────────────── Cardiovascular ───────────────────────────
    [
        "Coronary Artery Disease (Angina)",
        "chest pain or pressure, pain radiating to arm and jaw, shortness of breath, fatigue, sweating, dizziness, palpitations",
        "Arjuna bark powder (₹80 Rs) - Strengthens heart muscle; Ashwagandha (₹120 Rs) - Reduces stress; Garlic capsules (₹60 Rs) - Improves circulation",
        "Aspirin (₹10 Rs) - Antiplatelet; Atorvastatin (₹80 Rs) - Lowers cholesterol; Nitroglycerin (₹50 Rs) - Relieves chest pain",
        "Adopt a heart-healthy diet low in salt and fat. Exercise under supervision. Quit smoking. Manage stress and blood pressure. Emergency care for severe pain.",
        "Cardiologist"
    ],
    [
        "Heart Failure",
        "shortness of breath, swelling in legs and ankles, fatigue, rapid weight gain from fluid, persistent cough, wheezing, rapid heartbeat, abdominal swelling",
        "Arjuna (₹80 Rs) - Cardiac tonic; Punarnava (₹70 Rs) - Reduces fluid retention; Ashwagandha (₹120 Rs) - Supports heart function",
        "Furosemide (₹20 Rs) - Removes excess fluid; Enalapril (₹40 Rs) - Reduces heart load; Metoprolol (₹45 Rs) - Slows and strengthens heartbeat",
        "Follow a low-salt diet and monitor daily weight. Take medicines exactly as prescribed. Avoid alcohol and smoking. Regular cardiology follow-up.",
        "Cardiologist"
    ],
    [
        "Atrial Fibrillation",
        "irregular heartbeats, palpitations, racing heart, fatigue, shortness of breath, dizziness, chest discomfort, lightheadedness",
        "Arjuna (₹80 Rs) - Regulates heartbeat; Brahmi (₹90 Rs) - Calms the nervous system; Deep breathing with meditation",
        "Beta-blockers (Metoprolol ₹45 Rs) - Controls rate; blood thinners (Rivaroxaban ₹200 Rs) - Prevents stroke; cardioversion if needed",
        "Limit alcohol and caffeine. Manage stress and sleep well. Take blood thinners exactly as directed. Regular ECG monitoring.",
        "Cardiologist"
    ],
    [
        "High Cholesterol (Hyperlipidemia)",
        "often no symptoms, fatty deposits under skin (xanthomas), chest pain, fatigue, shortness of breath, yellowish patches near eyes",
        "Garlic capsules (₹60 Rs) - Lowers LDL; Guggulu (₹90 Rs) - Reduces cholesterol; Triphala (₹50 Rs) - Cleans the system",
        "Atorvastatin (₹80 Rs) - LDL lowering; Rosuvastatin (₹100 Rs) - Potent statin; lifestyle changes essential",
        "Reduce saturated fats and trans fats. Exercise 30-45 minutes daily. Eat fiber-rich foods and omega-3. Get lipid profile checked yearly.",
        "Cardiologist / Internal Medicine"
    ],
    [
        "Deep Vein Thrombosis",
        "swelling in one leg, pain and tenderness, warm skin, red discoloration, leg ache that worsens, visibly engorged veins",
        "Supportive anticoagulant herbs under guidance - Ginger (₹40 Rs) - Improves circulation; Garlic (₹60 Rs) - Blood thinner support",
        "Heparin injection (₹300 Rs) - Immediate anticoagulant; Warfarin (₹40 Rs) - Long-term thinning; compression stockings",
        "Seek urgent care if sudden chest pain or breathlessness. Take blood thinners as prescribed. Move regularly and avoid prolonged sitting. Use compression stockings.",
        "Vascular Surgeon / Cardiologist"
    ],
    [
        "Varicose Veins",
        "bulging twisted veins in legs, heavy aching legs, swelling in ankles, itchy skin over veins, leg cramps at night, skin discoloration",
        "Manjistha (₹80 Rs) - Improves circulation; Ashwagandha (₹120 Rs) - Reduces inflammation; Hirudotherapy oils for massage",
        "Compression stockings; Diosmin (₹90 Rs) - Improves vein tone; sclerotherapy or surgery for severe cases",
        "Elevate legs regularly. Avoid prolonged standing. Exercise to improve circulation. Wear compression stockings. Surgery for severe pain.",
        "Vascular Surgeon"
    ],
    [
        "Peripheral Artery Disease",
        "leg pain on walking that improves with rest, numbness or weakness in legs, cold lower leg, sores on feet that won't heal, pale skin, weak pulses",
        "Garlic (₹60 Rs) - Improves blood flow; Ashwagandha (₹120 Rs) - Circulation tonic; Guggulu (₹90 Rs) - Reduces artery inflammation",
        "Aspirin (₹10 Rs) - Antiplatelet; Atorvastatin (₹80 Rs) - Vascular protection; supervised walking programs",
        "Quit smoking completely. Walk daily as tolerated. Manage diabetes and blood pressure. Inspect feet daily for sores. See a vascular specialist.",
        "Vascular Surgeon / Cardiologist"
    ],
    [
        "Myocarditis",
        "chest pain, fever, fatigue, shortness of breath, rapid or irregular heartbeat, fluid retention with leg swelling, flu-like symptoms",
        "Strict rest; Arjuna (₹80 Rs) - Cardiac support after stabilization; Guduchi (₹60 Rs) - Reduces inflammation",
        "ACE inhibitors; beta-blockers; anti-inflammatory steroids; antiviral or antibiotics for cause",
        "Strict bed rest until recovery. Avoid strenuous exercise for months. Follow cardiologist follow-up. Report any chest pain or palpitations at once.",
        "Cardiologist"
    ],
    [
        "Pericarditis",
        "sharp chest pain worsening on breathing or lying down, relieved by sitting forward, fever, fatigue, cough, shortness of breath, palpitations",
        "Arjuna (₹80 Rs) - Heart support; Turmeric (₹40 Rs) - Anti-inflammatory; Rest and warm compress on chest",
        "Ibuprofen (₹25 Rs) - Reduces inflammation; Colchicine (₹80 Rs) - Prevents recurrence; steroids for resistant cases",
        "Rest and avoid heavy exertion. Take anti-inflammatories as directed. Avoid alcohol. Urgent care if pain is severe or breathing difficult.",
        "Cardiologist"
    ],

    # ─────────────────────────── Respiratory ───────────────────────────
    [
        "COPD (Chronic Obstructive Pulmonary Disease)",
        "chronic cough with mucus, shortness of breath that worsens, wheezing, chest tightness, frequent respiratory infections, low energy, weight loss",
        "Vasaka (₹60 Rs) - Expectorant; Kantakari (₹55 Rs) - Clears airways; Licorice (Mulethi) (₹45 Rs) - Soothes airways",
        "Salbutamol inhaler (₹120 Rs) - Bronchodilator; Tiotropium (₹180 Rs) - Long-acting bronchodilator; inhaled corticosteroids",
        "Quit smoking and avoid secondhand smoke. Use inhalers daily as prescribed. Do breathing exercises and pulmonary rehab. Get flu and pneumonia vaccines.",
        "Pulmonologist"
    ],
    [
        "Laryngitis",
        "hoarse voice, weak or lost voice, sore throat, dry cough, feeling of tickling in throat, fever, fatigue, dry scratchy throat",
        "Mulethi (Licorice) (₹45 Rs) - Soothes voice box; Honey and ginger tea (₹30 Rs) - Relieves irritation; Warm saline gargles (₹10 Rs)",
        "Voice rest; steam inhalation; lozenges; treat underlying infection if bacterial",
        "Rest your voice completely. Drink warm fluids. Avoid whispering and irritants. Humidify the air. See ENT if hoarseness lasts over 2 weeks.",
        "ENT Specialist (Otorhinolaryngologist)"
    ],
    [
        "Tonsillitis",
        "sore throat, white patches on tonsils, difficulty swallowing, fever, swollen tonsils, bad breath, ear pain, swollen neck glands",
        "Khadira (Akashia) gargles (₹40 Rs) - Antiseptic; Honey and turmeric (₹40 Rs) - Soothes inflammation; Tulsi tea (₹30 Rs) - Antipyretic",
        "Amoxicillin (₹50 Rs) - Antibiotic; Ibuprofen (₹25 Rs) - Pain and fever; warm salt water gargles",
        "Gargle with warm salt water. Drink warm fluids. Complete antibiotics. Rest. Surgery for recurrent tonsillitis when needed.",
        "ENT Specialist (Otorhinolaryngologist)"
    ],
    [
        "Pharyngitis (Sore Throat)",
        "sore raw throat, pain on swallowing, scratchy feeling, tonsil redness, fever, swollen glands, hoarseness, cold symptoms",
        "Honey and ginger (₹40 Rs) - Soothes throat; Licorice tea (₹45 Rs) - Anti-inflammatory; Tulsi gargles (₹30 Rs)",
        "Paracetamol (₹15 Rs) - Pain relief; lozenges; antibiotics only if bacterial (Amoxicillin ₹50 Rs)",
        "Gargle with warm salt water. Drink warm fluids with honey. Rest your voice. Avoid smoking and dry air. See doctor if strep suspected.",
        "General Physician / ENT"
    ],
    [
        "Croup",
        "barking cough especially at night, hoarse voice, fever, noisy breathing on inhale, runny nose, chest retractions in children",
        "Steam inhalation with Tulsi and eucalyptus (₹30 Rs) - Opens airways; warm onion-honey syrup (₹40 Rs) - Calms cough",
        "Dexamethasone (₹30 Rs) - Reduces airway swelling; racemic epinephrine for severe cases; humidified air",
        "Keep the child calm and upright. Use a humidifier or steam. Offer warm fluids. Seek emergency care if breathing difficulty worsens.",
        "Pediatrician"
    ],
    [
        "Pleurisy",
        "sharp chest pain worse on breathing or coughing, shortness of breath, fever, cough, pain radiating to shoulder, rapid breathing",
        "Vasaka syrup (₹65 Rs) - Lung support; Turmeric paste compress (₹40 Rs) - External pain relief; Guduchi (₹60 Rs) - Anti-inflammatory",
        "Ibuprofen (₹25 Rs) - Pain and inflammation; treat underlying cause (antibiotics for infection, anticoagulants for clot)",
        "Rest and avoid exertion. Take pain relief as directed. Treat the underlying cause. Urgent care for severe breathlessness.",
        "Pulmonologist / General Physician"
    ],
    [
        "Pulmonary Embolism",
        "sudden shortness of breath, sharp chest pain, cough with blood, rapid heartbeat, sweating, dizziness, fainting, anxiety",
        "This is an emergency; after stabilization supportive herbs including Arjuna (₹80 Rs) - Heart support",
        "Emergency: heparin (₹300 Rs) - Anticoagulant; thrombolytics for massive PE; long-term DOACs",
        "Call emergency services immediately. Take blood thinners as prescribed. Move legs during long travel. Stop smoking.",
        "Emergency Medicine / Pulmonologist"
    ],
    [
        "Sleep Apnea",
        "loud snoring, gasping or choking during sleep, daytime sleepiness, morning headaches, dry mouth on waking, irritability, poor concentration",
        "Ashwagandha (₹120 Rs) - Reduces stress; Shankhpushpi (₹70 Rs) - Calming; Nasal oil (Nasya) (₹60 Rs) - Opens airways",
        "CPAP machine therapy; oral appliances; weight-loss programs; surgery for obstructive causes",
        "Lose weight and avoid alcohol before bed. Sleep on your side. Use CPAP as prescribed. Avoid sedatives. Consult a sleep specialist.",
        "Sleep Medicine Specialist / Pulmonologist"
    ],
    [
        "COVID-19",
        "fever, dry cough, fatigue, loss of taste or smell, sore throat, headache, body aches, shortness of breath, chest tightness",
        "Giloy (₹60 Rs) - Immunity; Tulsi and honey kadha (₹30 Rs) - Soothing; Ashwagandha (₹120 Rs) - Recovery",
        "Antipyretics (Paracetamol ₹15 Rs); oxygen support in severe cases; antiviral therapy for high-risk patients",
        "Isolate and monitor oxygen levels. Rest and hydrate. Get vaccinated and boosted. Emergency care for breathing difficulty.",
        "General Physician / Infectious Disease Specialist"
    ],

    # ─────────────────────────── Gastrointestinal ───────────────────────────
    [
        "Gastroesophageal Reflux Disease (GERD)",
        "heartburn, acid regurgitation, chest pain, difficulty swallowing, chronic cough, hoarseness, sour taste in mouth, burping",
        "Avipattikar churna (₹70 Rs) - Balances acidity; Yashtimadhu (₹80 Rs) - Soothes stomach; Amla (₹40 Rs) - Natural antacid",
        "Omeprazole (₹30 Rs) - Suppresses acid; Antacids (₹50 Rs) - Quick relief; Domperidone (₹40 Rs) - Improves emptying",
        "Eat small frequent meals. Avoid lying down 3 hours after meals. Elevate your bed head. Avoid spicy, oily and acidic foods. Lose weight if overweight.",
        "Gastroenterologist"
    ],
    [
        "Appendicitis",
        "pain starting near navel then moving to lower right abdomen, sharp pain worsens with movement, nausea, vomiting, loss of appetite, fever, constipation or diarrhea",
        "This is a surgical emergency; warm the pain area only after surgeon's advice - post-op herbs like Kutki (₹100 Rs) - Healing",
        "Emergency appendectomy (surgery); IV antibiotics in hospital",
        "Seek emergency care immediately. Do not eat or drink and do not use laxatives. Surgery is the definitive treatment.",
        "Emergency Medicine / Surgeon"
    ],
    [
        "Gallstones",
        "sudden severe pain in upper right abdomen, pain after fatty meals, nausea, vomiting, pain radiating to right shoulder, bloating, jaundice if bile duct blocked",
        "Punarnava (₹70 Rs) - Anti-inflammatory; Varuna (₹85 Rs) - Dissolves stones; Trikatu (₹40 Rs) - Aids fat digestion",
        "Pain relievers (Diclofenac ₹25 Rs); ursodeoxycholic acid (₹80 Rs) - Dissolves small stones; surgery (cholecystectomy) if recurrent",
        "Limit fatty and fried foods. Maintain a healthy weight. Eat high-fiber foods. Seek urgent care for jaundice or severe pain. Surgery for recurring attacks.",
        "Gastroenterologist / Surgeon"
    ],
    [
        "Cirrhosis of the Liver",
        "fatigue, weakness, easy bruising, swelling in legs and abdomen, jaundice, itchy skin, confusion, weight loss, dark urine, spider angiomas",
        "Kutki (₹100 Rs) - Liver protective; Bhumi Amla (₹70 Rs) - Regenerative; Punarnava (₹70 Rs) - Reduces fluid",
        "Diuretics (Spironolactone ₹45 Rs) - Fluid removal; beta-blockers - prevent bleeding; lactulose for confusion; liver transplant in advanced cases",
        "Stop alcohol completely. Low-salt diet. Monitor for swelling and confusion. Regular specialist follow-up. Vaccinate against hepatitis A and B.",
        "Hepatologist / Gastroenterologist"
    ],
    [
        "Celiac Disease",
        "diarrhea, bloating, gas, weight loss, fatigue, anemia, itchy skin rash, abdominal pain, bone or joint pain, mouth ulcers",
        "Shatavari (₹90 Rs) - Heals intestinal lining; Yashtimadhu (₹80 Rs) - Soothes gut; Triphala (₹50 Rs) - Digestive balance",
        "Strict gluten-free diet; vitamin and mineral supplements (B12, iron, calcium); no specific drug therapy",
        "Follow a strict lifelong gluten-free diet. Read food labels for hidden gluten. Supplements for deficiencies. Regular follow-up and bone-density tests.",
        "Gastroenterologist / Nutritionist"
    ],
    [
        "Crohn's Disease",
        "chronic diarrhea, abdominal pain, weight loss, fatigue, fever, mouth sores, reduced appetite, blood in stool, joint pain",
        "Kutajarishta (₹80 Rs) - Calms gut; Slippery elm-like soothing herbs (Aloe) (₹45 Rs) - Coats intestine; Ashwagandha (₹120 Rs) - Restoration",
        "Mesalamine (₹95 Rs) - Reduces gut inflammation; steroids (Budesonide ₹150 Rs); biologics (Infliximab) for severe disease",
        "Follow a nutritionist-guided diet and food diary. Avoid NSAIDs and smoking. Manage stress. Take immunomodulators exactly as prescribed.",
        "Gastroenterologist"
    ],
    [
        "Ulcerative Colitis",
        "bloody diarrhea, abdominal cramps, rectal pain, urgency to defecate, weight loss, fatigue, fever, reduced appetite",
        "Kutajarishta (₹80 Rs) - Controls diarrhea; Dhanyaka (Coriander) (₹20 Rs) - Soothes gut; Shatavari (₹90 Rs) - Healing",
        "Mesalamine (₹95 Rs) - First-line; steroids for flares; immunomodulators (Azathioprine ₹100 Rs)",
        "Follow the prescribed medication plan. Keep a food diary and avoid triggers. Stay hydrated. Regular colonoscopies for monitoring.",
        "Gastroenterologist"
    ],
    [
        "Constipation",
        "fewer than three bowel movements a week, hard dry stools, straining, bloating, abdominal discomfort, feeling of incomplete evacuation, small stools",
        "Triphala (₹50 Rs) - Gentle laxative; Castor oil (warm) (₹30 Rs) - Lubricant; Isabgol (Psyllium) (₹30 Rs) - Bulk-forming fiber",
        "Lactulose (₹45 Rs) - Osmotic laxative; Bisacodyl (₹20 Rs) - Stimulant laxative; stool softeners",
        "Drink 2-3 liters of water daily. Eat fiber-rich fruits and vegetables. Exercise regularly. Set a regular toilet routine. Avoid delaying the urge.",
        "Gastroenterologist / General Physician"
    ],
    [
        "Hemorrhoids (Piles)",
        "bleeding during bowel movements, painful lump near anus, itching and irritation, swelling around anus, pain and discomfort, painless bright red blood",
        "Dhak (Palash) flowers (₹50 Rs) - Stops bleeding; Avipattikar churna (₹70 Rs) - Regulates digestion; Warm sitz bath with Triphala (₹30 Rs)",
        "Hydrocortisone cream (₹35 Rs) - Reduces swelling; stool softeners; rubber band ligation; surgery for large piles",
        "Eat high-fiber foods and drink water. Avoid straining on the toilet. Warm sitz baths daily. Don't sit too long. Severe bleeding needs a doctor.",
        "Gastroenterologist / Surgeon"
    ],
    [
        "Pancreatitis",
        "severe upper abdominal pain radiating to the back, nausea, vomiting, fever, rapid pulse, swollen tender abdomen, oily stools",
        "Emergency care; later supportive herbs - Ginger (₹40 Rs) - Anti-inflammatory; Shatavari (₹90 Rs) - Restores digestion",
        "IV fluids and pain control in hospital; Pancreatic enzyme supplements (₹150 Rs); treat the underlying cause",
        "Seek urgent hospital care for severe pain. Stop alcohol completely. Follow a low-fat diet. Quit smoking. Manage gallstones and triglycerides.",
        "Gastroenterologist"
    ],
    [
        "Food Allergy",
        "hives, swelling of lips and tongue, itching, abdominal pain, diarrhea, nausea, wheezing, dizziness, anaphylaxis in severe cases",
        "Emergency antihistamine herbs are not sufficient; after care - Amalaki (₹50 Rs) - Immune balance; Yashtimadhu (₹80 Rs) - Soothes",
        "Epinephrine auto-injector (₹450 Rs) - For anaphylaxis; antihistamines (Cetirizine ₹20 Rs); avoidance is key",
        "Identify and strictly avoid the offending food. Read labels carefully. Carry an epinephrine auto-injector if advised. Tell restaurants about allergies.",
        "Allergist / Immunologist"
    ],
    [
        "Non-Alcoholic Fatty Liver Disease (NAFLD)",
        "fatigue, mild right upper abdomen discomfort, unexplained weight gain, high triglycerides, enlarged liver, no symptoms in early stage",
        "Kutki (₹100 Rs) - Liver detox; Bhumi Amla (₹70 Rs) - Liver health; Triphala (₹50 Rs) - Metabolic balance",
        "Vitamin E in select cases; diabetes and cholesterol medications; weight management is the mainstay",
        "Lose 5-10% of body weight gradually. Cut sugar and refined carbs. Exercise 150 minutes weekly. Avoid alcohol. Repeat liver tests regularly.",
        "Hepatologist / Gastroenterologist"
    ],
    [
        "Diverticulitis",
        "left lower abdominal pain, fever, nausea, vomiting, change in bowel habits, bloating, tenderness, constipation or diarrhea",
        "Liquid diet and rest initially; after acute phase - Kutajarishta (₹80 Rs) - Gut healing; Yashtimadhu (₹80 Rs) - Anti-inflammatory",
        "Antibiotics (Ciprofloxacin + Metronidazole ₹90 Rs); clear liquid diet; surgery for complications",
        "Temporarily follow a clear-liquid diet. Take full antibiotics course. Later add fiber slowly. See a doctor for fever or severe pain.",
        "Gastroenterologist"
    ],
    [
        "Dysentery (Amoebic)",
        "blood and mucus in stool, frequent loose stools, abdominal cramps, tenesmus, fever, weakness, nausea, dehydration",
        "Kutajarishta (₹80 Rs) - Controls dysentery; Pomegranate rind tea (₹40 Rs) - Astringent; Bilva (Bael) (₹50 Rs) - Gut tonic",
        "Metronidazole (₹35 Rs) - Antibiotic for amoeba; ORS for dehydration; rehydration salts",
        "Drink boiled water and ORS. Complete antibiotic course. Wash hands after toilet. Avoid raw foods in unhygienic settings.",
        "General Physician / Gastroenterologist"
    ],
    [
        "Lactose Intolerance",
        "bloating, gas, diarrhea after dairy, stomach cramps, nausea, rumbling sounds, loose stools, symptoms after milk products",
        "Ginger infusion (₹30 Rs) - Improves digestion; Trikatu (₹40 Rs) - Digestive fire; Amalaki (₹50 Rs) - Balances",
        "Lactase enzyme tablets (₹80 Rs); calcium and vitamin D supplements; dietary lactose avoidance",
        "Reduce or avoid dairy, or choose lactose-free products. Take lactase tablets before dairy. Ensure adequate calcium from other sources.",
        "Gastroenterologist / Nutritionist"
    ],

    # ─────────────────────────── Neurology and mental health ───────────────────────────
    [
        "Tension Headache",
        "dull pressure or tight band pain around head, both-sided headache, neck and shoulder tightness, pain worsening late day, sensitivity to noise",
        "Brahmi (₹90 Rs) - Calms the mind; Shankhpushpi (₹70 Rs) - Relaxation; Massage oil on scalp and neck (₹60 Rs)",
        "Ibuprofen (₹25 Rs) - Pain relief; muscle relaxants if needed; stress management",
        "Practice relaxation techniques and deep breathing. Maintain good posture. Use warm compresses on neck. Ensure regular sleep and meals.",
        "Neurologist / General Physician"
    ],
    [
        "Cluster Headache",
        "severe one-sided head pain around the eye, red watery eye, nasal congestion on one side, restlessness, attacks in clusters, for hours for weeks",
        "Acute-phase supportive care; preventive - Brahmi (₹90 Rs) - Nerve support; Dashamoola massage (₹100 Rs)",
        "Oxygen inhalation; Sumatriptan injection (₹150 Rs); Verapamil (₹60 Rs) - Preventive",
        "Avoid alcohol and smoking during cluster periods. Use oxygen as instructed. Follow preventive medication as prescribed. Keep an attack diary.",
        "Neurologist"
    ],
    [
        "Epilepsy",
        "recurrent seizures, convulsions, jerking of limbs, staring spells, confusion after seizure, sudden falls, loss of consciousness, aura before seizure",
        "Brahmi (₹90 Rs) - Nerve stabilizer; Ashwagandha (₹120 Rs) - Stress reduction; Shankhpushpi (₹70 Rs) - Sedative",
        "Sodium valproate (₹55 Rs) - Anti-seizure; Levetiracetam (₹140 Rs) - Modern anticonvulsant; carbamazepine",
        "Take anti-seizure medicines regularly, never skip. Avoid alcohol and sleep deprivation. If a seizure lasts 5 minutes, call emergency services. Wear medical alert ID.",
        "Neurologist"
    ],
    [
        "Parkinson's Disease",
        "tremor in hands at rest, slow movements, stiff muscles, impaired posture and balance, loss of facial expression, soft or slurred speech, reduced arm swing",
        "Kapikachhu (Mucuna) (₹90 Rs) - Natural levodopa; Ashwagandha (₹120 Rs) - Supports nerves; Brahmi (₹90 Rs) - Cognitive support",
        "Levodopa-Carbidopa (₹120 Rs) - Dopamine replacement; dopamine agonists (Pramipexole ₹110 Rs)",
        "Exercise daily with physiotherapy. Follow medication timing strictly. Adjust diet to avoid protein-medication interaction. Join support groups.",
        "Neurologist"
    ],
    [
        "Stroke (Cerebrovascular Accident)",
        "sudden one-sided weakness or numbness, facial drooping, slurred speech, sudden confusion, severe headache, vision loss in one eye, difficulty walking, dizziness",
        "This is an emergency; after recovery - Arjuna (₹80 Rs) - Circulation; Brahmi (₹90 Rs) - Brain recovery; Ashwagandha (₹120 Rs)",
        "Emergency: clot-busting r-tPA within hours; blood thinners (Aspirin ₹10 Rs); statins; blood pressure control",
        "Call emergency services immediately at first signs (FAST: Face, Arm, Speech, Time). Rehabilitation is crucial. Control BP, diabetes, and cholesterol. Quit smoking.",
        "Emergency Medicine / Neurologist"
    ],
    [
        "Alzheimer's Disease",
        "memory loss disrupting daily life, confusion with time and place, difficulty with problem solving, misplacing things, withdrawal, mood changes, poor judgment",
        "Brahmi (₹90 Rs) - Memory support; Ashwagandha (₹120 Rs) - Mental calm; Shankhpushpi (₹70 Rs) - Cognitive tonic",
        "Donepezil (₹100 Rs) - Cholinesterase inhibitor; Memantine (₹130 Rs) - For moderate disease",
        "Maintain routine and familiar surroundings. Keep mentally and physically active. Manage other health conditions. Caregiver support is essential.",
        "Neurologist / Geriatrician"
    ],
    [
        "Multiple Sclerosis",
        "numbness or weakness in limbs, tingling, blurred vision, double vision, lack of coordination, fatigue, dizziness, bladder problems, spasticity",
        "Ashwagandha (₹120 Rs) - Immune balance; Guduchi (₹60 Rs) - Modulates immunity; Brahmi (₹90 Rs) - Nerve support",
        "Corticosteroids for flares (Methylprednisolone); disease-modifying therapy (Interferon β, ₹450 Rs); physiotherapy",
        "Follow your disease-modifying therapy. Physiotherapy for mobility. Manage stress and avoid overheating. Regular neurology follow-up.",
        "Neurologist"
    ],
    [
        "Bell's Palsy",
        "sudden one-sided facial weakness, drooping eyelid and mouth, difficulty smiling or closing eye, drooling, ear pain, altered taste, dry eye",
        "Bala oil massage (₹120 Rs) - Nerve strengthening; Mahanarayan oil (₹130 Rs) - Facial massage; Bacopa (₹90 Rs) - Nerve recovery",
        "Prednisolone (₹50 Rs) - Within 72 hours improves recovery; artificial tears for the eye",
        "Start steroids early. Protect the weak eye with eye drops and taping at night. Do gentle facial exercises. Most recover within months.",
        "Neurologist"
    ],
    [
        "Vertigo (BPPV)",
        "spinning sensation triggered by head movement, loss of balance, nausea, vomiting, unsteady gait, dizziness lasting seconds to a minute",
        "Ashwagandha (₹120 Rs) - Balance support; Brahmi (₹90 Rs) - Calms inner ear nerves; Nimba head oil massage (₹60 Rs)",
        "Epley manoeuvre by a specialist; Betahistine (₹45 Rs) - Improves inner ear circulation; antihistamines for symptoms",
        "Perform the Epley manoeuvre with guidance. Avoid sudden head movements. Sit up slowly. Sleep with head slightly elevated. See ENT for persistent vertigo.",
        "ENT / Neurologist"
    ],
    [
        "Peripheral Neuropathy",
        "numbness and tingling in hands or feet, sharp burning pain, sensitivity to touch, muscle weakness, loss of balance, worsened at night",
        "Bala (₹70 Rs) - Nerve tonic; Ashwagandha (₹120 Rs) - Nerve repair; Massage with Mahanarayan oil (₹130 Rs)",
        "Pregabalin (₹70 Rs) - Nerve pain; Amitriptyline (₹50 Rs) - Low-dose pain relief; vitamin B12 supplements",
        "Manage the underlying cause (diabetes control). Take pain medicines as prescribed. Check feet daily for injuries. Limit alcohol.",
        "Neurologist"
    ],
    [
        "Anxiety Disorder",
        "excessive worry, restlessness, irritability, difficulty concentrating, racing heart, muscle tension, sleep problems, sweating, feeling overwhelmed, avoiding situations",
        "Ashwagandha (₹120 Rs) - Stress adaptogen; Brahmi (₹90 Rs) - Calms mind; Shankhpushpi (₹70 Rs) - Relaxing",
        "SSRIs (Escitalopram ₹70 Rs) - Long-term relief; short-term benzodiazepines; cognitive behavioral therapy",
        "Practice deep breathing and mindfulness. Regular exercise. Limit caffeine and alcohol. Consistent sleep schedule. Consider therapy.",
        "Psychiatrist / Clinical Psychologist"
    ],
    [
        "Depression",
        "persistent sadness, loss of interest in activities, fatigue, sleep disturbance, appetite changes, feelings of worthlessness, poor concentration, thoughts of self-harm",
        "Ashwagandha (₹120 Rs) - Mood support; Brahmi (₹90 Rs) - Mental clarity; Jatamansi (₹90 Rs) - Calming",
        "SSRIs (Sertraline ₹60 Rs); psychotherapy (CBT); exercise therapy",
        "Seek professional help. Take antidepressants as prescribed. Maintain routine and support network. If you have thoughts of self-harm, contact emergency services now.",
        "Psychiatrist / Clinical Psychologist"
    ],
    [
        "Bipolar Disorder",
        "manic episodes with elevated mood, high energy, reduced need for sleep, grandiosity, rapid speech; depressive episodes with low mood, hopelessness, fatigue",
        "Supportive - Brahmi (₹90 Rs) - Mood balance; Ashwagandha (₹120 Rs) - Stability; regulated daily routine with meditation",
        "Lithium (₹80 Rs) - Mood stabilizer; Lamotrigine (₹110 Rs); antipsychotics for mania",
        "Take mood stabilizers consistently, never stop abruptly. Regular blood tests for lithium levels. Maintain a stable sleep pattern. Involve family in care.",
        "Psychiatrist"
    ],
    [
        "Schizophrenia",
        "hallucinations (hearing voices), delusions, disorganized speech, social withdrawal, reduced motivation, poor self-care, difficulty expressing emotion",
        "Supportive Ayurvedic care only - Brahmi (₹90 Rs) - Calming; Ashwagandha (₹120 Rs) - Reducing stress; family support and routine",
        "Antipsychotics (Risperidone ₹70 Rs, Olanzapine ₹60 Rs); long-acting injectables; psychosocial rehabilitation",
        "Stick to antipsychotic medication without interruption. Attend follow-ups. Build a supportive environment. Avoid alcohol and recreational drugs.",
        "Psychiatrist"
    ],
    [
        "ADHD (Attention Deficit Hyperactivity Disorder)",
        "inattention easily distracted, difficulty organising tasks, forgetfulness, fidgeting, excessive talking, interrupting, poor time management, impulsivity",
        "Brahmi (₹90 Rs) - Improves focus; Shankhpushpi (₹70 Rs) - Calms restlessness; structured daily routine",
        "Stimulants (Methylphenidate ₹80 Rs); non-stimulant (Atomoxetine ₹120 Rs); behavioral therapy",
        "Follow treatment and therapy plan. Use routines and reminders. Minimize distractions while studying. Regular exercise improves symptoms.",
        "Psychiatrist / Pediatrician"
    ],
    [
        "Obsessive Compulsive Disorder (OCD)",
        "unwanted repeated thoughts (obsessions), repetitive rituals (compulsions), checking and washing behaviors, distress when rituals are disrupted, hoarding",
        "Brahmi (₹90 Rs) - Reduces mental rigidity; Ashwagandha (₹120 Rs) - Lowers anxiety; Jatamansi (₹90 Rs) - Calming",
        "SSRIs (Fluoxetine ₹55 Rs) - High dose; cognitive behavioral therapy with ERP; antipsychotic augmentation",
        "Commit to Cognitive Behavioral Therapy (ERP). Take SSRIs as prescribed. Avoid rituals gradually with therapist guidance. Family support helps.",
        "Psychiatrist / Clinical Psychologist"
    ],
    [
        "Panic Disorder",
        "sudden intense fear attacks, racing heart, sweating, trembling, shortness of breath, chest tightness, dizziness, fear of losing control, avoidance of situations",
        "Ashwagandha (₹120 Rs) - Calms nervous system; Brahmi (₹90 Rs) - Panic support; Slow breathing with peppermint oil (₹40 Rs)",
        "SSRIs (Sertraline ₹60 Rs); CBT; short-term benzodiazepines only during recovery",
        "Learn breathing and grounding techniques. Exercise regularly. Limit caffeine. Attend therapy. Take medication as directed.",
        "Psychiatrist / Clinical Psychologist"
    ],
    [
        "Post-Traumatic Stress Disorder (PTSD)",
        "flashbacks, nightmares, intrusive memories, avoiding reminders, hypervigilance, irritability, difficulty sleeping, emotional numbness",
        "Ashwagandha (₹120 Rs) - Stress adaptogen; Brahmi (₹90 Rs) - Mental calm; Jatamansi (₹90 Rs) - Sleep support",
        "SSRIs (Sertraline ₹60 Rs, Paroxetine ₹75 Rs); trauma-focused therapy (CBT/EMDR)",
        "Engage in trauma-focused therapy. Take medication as prescribed. Build a support system. Practice grounding techniques and regular sleep.",
        "Psychiatrist / Clinical Psychologist"
    ],
    [
        "Restless Legs Syndrome",
        "uncontrollable urge to move legs especially at night, creeping or crawling sensations, symptoms worse at rest, relief with movement, sleep disturbance",
        "Ashwagandha (₹120 Rs) - Calming; Bala oil massage (₹120 Rs) - Leg relaxation; warm foot baths with Epsom salts (₹30 Rs)",
        "Dopamine agonists (Ropinirole ₹90 Rs); gabapentin for sleep; iron supplements if deficient",
        "Check iron levels and supplement if low. Avoid caffeine and alcohol. Leg stretches and warm baths at bedtime. Maintain a sleep routine.",
        "Neurologist / Sleep Specialist"
    ],

    # ─────────────────────────── Endocrine / metabolic ───────────────────────────
    [
        "Hyperthyroidism",
        "rapid heartbeat, weight loss despite normal appetite, sweating, tremors, anxiety, heat intolerance, frequent bowel movements, fatigue, bulging eyes",
        "Shanka pushpi (₹70 Rs) - Calms nerves; Ashwagandha (₹120 Rs) - Balances thyroid; Punarnava (₹70 Rs) - Anti-inflammatory",
        "Methimazole (₹60 Rs) - Reduces thyroid hormone; beta-blockers for symptoms; radioiodine or surgery for some",
        "Take antithyroid medicine regularly. Get TSH levels checked periodically. Avoid excess iodine. Manage stress and get enough rest.",
        "Endocrinologist"
    ],
    [
        "Hashimoto's Thyroiditis",
        "fatigue, weight gain, cold intolerance, dry skin, hair thinning, constipation, muscle aches, depression, goiter, heavy menstruation",
        "Ashwagandha (₹120 Rs) - Balances thyroid; Kanchanar guggulu (₹100 Rs) - Supports thyroid; Triphala (₹50 Rs) - Metabolism",
        "Levothyroxine (₹30 Rs) - Hormone replacement; regular TSH monitoring",
        "Take levothyroxine on an empty stomach each morning. Avoid soy near medication time. Regular TSH tests. Manage stress and sleep.",
        "Endocrinologist"
    ],
    [
        "Goiter (Enlarged Thyroid)",
        "swelling at the base of the neck, tightness in throat, cough, hoarseness, difficulty swallowing, breathing difficulty with large goiter",
        "Kanchanar guggulu (₹100 Rs) - Reduces gland swelling; Ashwagandha (₹120 Rs) - Thyroid balance; Varuna (₹85 Rs) - Supports neck glands",
        "Levothyroxine (₹30 Rs) if hypothyroid; iodine as appropriate; surgery for obstructive goiter",
        "Get thyroid function and ultrasound checked. Take medicines as prescribed. Ensure adequate (not excess) iodine. Surgery if swallowing becomes hard.",
        "Endocrinologist"
    ],
    [
        "Polycystic Ovary Syndrome (PCOS)",
        "irregular or missed periods, excess facial hair, acne, weight gain, hair thinning on scalp, difficulty conceiving, dark skin patches, mood changes",
        "Shatavari (₹90 Rs) - Hormonal balance; Ashwagandha (₹120 Rs) - Reduces insulin resistance; Kanchanar guggulu (₹100 Rs) - Cysts",
        "Metformin (₹35 Rs) - Improves insulin sensitivity; hormonal birth control for cycle regulation; fertility treatments if trying to conceive",
        "Lose 5-10% body weight with diet and exercise. Follow low-glycemic meals. Manage stress. Regular gynaecologist follow-up.",
        "Gynaecologist / Endocrinologist"
    ],
    [
        "Type 1 Diabetes",
        "excessive thirst, frequent urination, extreme hunger, unexplained weight loss, fatigue, blurry vision, dry mouth, fruity-smelling breath",
        "Karela juice (₹50 Rs) - Supports sugar control; Jamun seed powder (₹60 Rs) - Helps glucose; Fenugreek (₹30 Rs)",
        "Insulin injections (₹250 Rs) - Essential; regular blood glucose monitoring",
        "Insulin is essential - never miss doses. Monitor blood sugar frequently. Count carbohydrates and balance with insulin. Have a sick-day plan.",
        "Endocrinologist"
    ],
    [
        "Hypoglycemia",
        "shakiness, sweating, rapid heartbeat, confusion, dizziness, hunger, irritability, blurred vision, seizure or unconsciousness in severe cases",
        "Post-event restoration - Guduchi (₹60 Rs); Ashwagandha (₹120 Rs) - Blood sugar balance",
        "Immediate: fast-acting glucose (glucose tablets / juice); glucagon injection for emergencies",
        "Treat immediately with 15g fast carbs and re-check in 15 minutes. Eat regular balanced meals. Let family know how to give glucagon.",
        "Endocrinologist / General Physician"
    ],
    [
        "Osteoporosis",
        "no symptoms until fracture, back pain from vertebral crush, loss of height over time, stooped posture, easy fractures of wrist hip spine",
        "Ashwagandha (₹120 Rs) - Bone strength; Godanti bhasma (₹90 Rs) - Calcium source; Tila (sesame) seeds (₹40 Rs) - Bone nutrition",
        "Calcium and vitamin D supplements; bisphosphonates (Alendronate ₹100 Rs); HRT in select cases",
        "Ensure calcium (1000-1200 mg) and vitamin D daily. Weight-bearing exercises. Avoid smoking and excess alcohol. Get a DEXA scan for at-risk people.",
        "Endocrinologist / Orthopedic Surgeon"
    ],
    [
        "Gout",
        "sudden severe joint pain usually in big toe, swelling, redness, warmth, tenderness, recurrent attacks, difficulty walking",
        "Guduchi (₹60 Rs) - Reduces uric acid inflammation; Punarnava (₹70 Rs) - Purifies blood; Ginger compress (₹40 Rs)",
        "Colchicine (₹30 Rs) - Acute attack relief; Allopurinol (₹50 Rs) - Prevents attacks; NSAIDs (Naproxen ₹30 Rs)",
        "Drink plenty of water. Limit purine-rich foods (red meat, organ meats, seafood) and alcohol. Manage weight. Take urate-lowering medicines regularly.",
        "Rheumatologist"
    ],
    [
        "Addison's Disease",
        "fatigue, weakness, weight loss, low blood pressure with dizziness, darkening of skin, salt craving, abdominal pain, nausea, depression",
        "Supportive - Ashwagandha (₹120 Rs) - Adrenal support; Shatavari (₹90 Rs) - Energy; Punarnava (₹70 Rs) - Electrolyte balance",
        "Hydrocortisone (₹80 Rs) - Steroid replacement; fludrocortisone (₹60 Rs) - Salt/fluid balance",
        "Never stop steroid replacement. Double the dose during illness or stress (sick-day rules). Wear a medical alert bracelet. Carry hydrocortisone injection training.",
        "Endocrinologist"
    ],
    [
        "Vitamin D Deficiency",
        "bone pain, muscle weakness, fatigue, mood changes, frequent infections, hair loss, slow wound healing, joint stiffness",
        "Tila (sesame) (₹40 Rs) - Calcium and D support; Ashwagandha (₹120 Rs) - Strength; Sun exposure with morning sun",
        "Vitamin D3 supplements (₹60 Rs); calcium combined therapy; treat underlying cause",
        "Get 15-20 minutes of midday sunlight daily. Take supplements as prescribed. Eat fortified foods. Repeat blood test after 3 months.",
        "General Physician / Endocrinologist"
    ],
    [
        "Vitamin B12 Deficiency",
        "weakness, fatigue, numbness and tingling in hands and feet, pale skin, sore tongue, confusion, memory problems, balance issues, shortness of breath",
        "Ashwagandha (₹120 Rs) - Nerve strength; Bala (₹70 Rs) - Tonic; green leafy vegetables in diet",
        "Vitamin B12 injections (₹80 Rs) or high-dose oral supplements; treat underlying cause",
        "Take B12 as prescribed (tablets or injections). Include fortified foods. For vegans, lifelong supplementation is needed. Repeat blood tests.",
        "General Physician / Hematologist"
    ],

    # ─────────────────────────── Renal / urology ───────────────────────────
    [
        "Chronic Kidney Disease (CKD)",
        "fatigue, swelling in feet and ankles, puffiness around eyes, poor appetite, nausea, drowsiness, muscle cramps, Itching, reduced urine output, foamy urine",
        "Punarnava (₹70 Rs) - Supports kidneys; Gokshura (₹80 Rs) - Kidney tonic; Varuna (₹85 Rs) - Detoxifies",
        "ACE inhibitors / ARBs (₹60 Rs) - Protect kidneys; diuretics; erythropoietin for anemia; dialysis in advanced stage",
        "Control blood pressure and diabetes strictly. Low-sodium, low-protein diet. Avoid NSAIDs and self-medication. Regular nephrologist follow-up.",
        "Nephrologist"
    ],
    [
        "Glomerulonephritis",
        "blood in urine (pink or cola-colored), foamy urine, swelling in face and legs, high blood pressure, reduced urine output, fatigue",
        "Punarnava (₹70 Rs) - Kidney health; Gokshura (₹80 Rs) - Urinary tonic; Varuna (₹85 Rs) - Anti-inflammatory",
        "Blood pressure medicines (ACE inhibitors); steroids or immunosuppressants; diuretics for swelling",
        "Strictly control blood pressure. Low-salt diet. Rest during acute phase. Treat strep infections promptly. Regular kidney function tests.",
        "Nephrologist"
    ],
    [
        "Pyelonephritis (Kidney Infection)",
        "high fever with chills, flank or back pain, painful urination, frequent urination, nausea, vomiting, cloudy or foul-smelling urine, blood in urine",
        "Gokshura (₹80 Rs) - Urinary tract support; Punarnava (₹70 Rs) - Anti-inflammatory; Coriander seed water (₹20 Rs) - Cooling",
        "Antibiotics (Ciprofloxacin ₹40 Rs); IV antibiotics for severe cases; pain relievers",
        "Complete the full antibiotic course. Drink plenty of water. Rest. Repeat urine test after treatment. Urgent care for high fever and vomiting.",
        "Urologist / Nephrologist"
    ],
    [
        "Nephrotic Syndrome",
        "severe swelling in legs and around eyes, foamy urine, weight gain from fluid, fatigue, loss of appetite, high cholesterol",
        "Punarnava (₹70 Rs) - Reduces fluid; Gokshura (₹80 Rs) - Kidney health; Shatavari (₹90 Rs) - Protein restoration",
        "Steroids (Prednisolone ₹50 Rs); diuretics; ACE inhibitors; anticoagulants if needed",
        "Low-salt diet with controlled protein. Take steroids exactly as prescribed. Monitor weight daily. Regular urine protein tests.",
        "Nephrologist"
    ],
    [
        "Benign Prostatic Hyperplasia (BPH)",
        "frequent urination especially at night, difficulty starting urination, weak stream, dribbling, urgency, feeling of incomplete emptying, straining to urinate",
        "Gokshura (₹80 Rs) - Supports prostate; Ashwagandha (₹120 Rs) - Strengthens pelvic muscles; Saw palmetto-like herbal (Punarnava) (₹70 Rs)",
        "Alpha-blockers (Tamsulosin ₹45 Rs) - Relax prostate; 5-alpha reductase inhibitors (Finasteride ₹60 Rs); surgery if severe",
        "Limit fluids before bed. Avoid caffeine and alcohol. Don't delay urination. Empty bladder fully. Urology follow-up and PSA monitoring.",
        "Urologist"
    ],
    [
        "Prostatitis",
        "pain or burning on urination, frequent urgent urination, pain in pelvis or lower back, body aches, fever and chills, painful ejaculation, cloudy urine",
        "Gokshura (₹80 Rs) - Supports urinary health; Punarnava (₹70 Rs) - Anti-inflammatory; Jatamansi (₹90 Rs) - Pain relief",
        "Antibiotics (Ciprofloxacin ₹40 Rs, Doxycycline ₹70 Rs); alpha-blockers; anti-inflammatories",
        "Finish all antibiotics. Drink plenty of fluids. Warm sitz baths for comfort. Avoid alcohol and spicy food. Rest during acute phase.",
        "Urologist"
    ],
    [
        "Erectile Dysfunction",
        "difficulty achieving or maintaining erection, reduced sexual desire, premature ejaculation, performance anxiety, underlying diabetes or heart disease",
        "Ashwagandha (₹120 Rs) - Libido and stamina; Kapikachhu (₹90 Rs) - Improves sexual function; Shatavari (₹90 Rs) - Balance",
        "Sildenafil (₹70 Rs) - On-demand therapy; Tadalafil (₹90 Rs); treat underlying cardiovascular cause; psychosexual therapy",
        "Address the underlying cause (diabetes, heart disease, stress). Exercise regularly. Limit alcohol and smoking. Openly consult your doctor.",
        "Urologist / Sexologist"
    ],

    # ─────────────────────────── ENT / eye ───────────────────────────
    [
        "Otitis Media (Middle Ear Infection)",
        "ear pain especially at night, tugging at ear in children, fever, fluid draining from ear, difficulty hearing, irritability, poor sleep",
        "Warm garlic oil drops (₹40 Rs) - Antibacterial; Neem drops (₹35 Rs) - Antiseptic; Dashamoola (₹90 Rs) - Reduces inflammation",
        "Amoxicillin (₹50 Rs) - Antibiotic; Paracetamol (₹15 Rs) - Pain and fever; ear drops if eardrum is intact only on advice",
        "Finish the full antibiotic course. Apply warm compress to the ear. Keep ears dry. See ENT if pain persists or fluid drains.",
        "ENT Specialist (Otorhinolaryngologist)"
    ],
    [
        "Tinnitus",
        "ringing, buzzing, hissing or roaring sound in ears, ringing worse in silence, hearing loss, dizziness, difficulty concentrating, sleep disturbance",
        "Brahmi (₹90 Rs) - Inner ear nerve support; Ashwagandha (₹120 Rs) - Stress relief; white noise with relaxing music",
        "Treat underlying cause; hearing aids for hearing loss; sound therapy; stress management and low-dose medication",
        "Avoid loud noises and use ear protection. Reduce caffeine and alcohol. Manage stress with relaxation. Mask the sound with white noise.",
        "ENT Specialist (Otorhinolaryngologist)"
    ],
    [
        "Cataract",
        "blurry or cloudy vision, sensitivity to light and glare, fading of colors, trouble with night vision, halos around lights, frequent prescription changes",
        "Triphala eye wash (₹50 Rs) - Eye tonic; Amalaki (₹50 Rs) - Antioxidant; Licorice drops (₹40 Rs) - Cooling",
        "Cataract surgery with lens implant; no medication dissolves cataract",
        "Use sunglasses to reduce glare. Get regular eye checks. Managing diabetes well. Surgery is safe and restores vision when ready.",
        "Ophthalmologist"
    ],
    [
        "Glaucoma",
        "often no early symptoms, gradual loss of peripheral vision, tunnel vision, eye pain, halos around lights, headache, red eye, blurred vision",
        "Triphala eye wash (₹50 Rs) - Eye health; Jyotishmati oil (₹70 Rs) - Optic nerve support; Manage stress and sleep",
        "Latanoprost eye drops (₹120 Rs) - Reduce eye pressure; timolol drops; laser or surgery if needed",
        "Use eye drops daily without skipping. Regular eye-pressure monitoring. Avoid heavy lifting and inverted postures. Family history needs screening.",
        "Ophthalmologist"
    ],
    [
        "Age-Related Macular Degeneration",
        "blurred central vision, difficulty reading, colors looking dull, difficulty recognizing faces, straight lines appearing wavy, dark spots in vision",
        "Amalaki (₹50 Rs) - Antioxidant; Triphala (₹50 Rs) - Eye tonic; lutein-rich spinach and greens in diet",
        "Anti-VEGF injections for wet AMD (₹2500 Rs); vitamin supplements AREDS2; low-vision aids",
        "Eat leafy greens and omega-3s. Protect eyes from sun with sunglasses. Stop smoking. Regular retina examinations.",
        "Ophthalmologist (Retina Specialist)"
    ],
    [
        "Stye (Hordeolum)",
        "painful red bump on eyelid, swelling, tenderness, tearing, crusting on eyelid, feeling of something in eye, light sensitivity",
        "Warm Triphala compress (₹50 Rs) - Soothes; Rose water eye rinse (₹30 Rs); Neem water wash (₹25 Rs)",
        "Warm compresses; antibiotic eye drops (Moxifloxacin ₹80 Rs); rarely surgical drainage",
        "Apply warm compresses 4-5 times daily. Don't squeeze the stye. Wash hands and avoid eye makeup. See an eye doctor if it persists.",
        "Ophthalmologist"
    ],
    [
        "Dry Eye Syndrome",
        "burning or stinging eyes, feeling of grit in eyes, redness, blurred vision, tearing, discomfort in wind or screens, sensitivity to light",
        "Triphala eye wash (₹50 Rs) - Cooling; Rose water drops (₹30 Rs) - Soothes; Castor oil eye application at lid margin (₹40 Rs)",
        "Artificial tears (₹80 Rs); cyclosporine eye drops for inflammation; punctal plugs if severe",
        "Blink often and take screen breaks (20-20-20 rule). Use a humidifier. Protect eyes in wind and sun. Warm lid compresses.",
        "Ophthalmologist"
    ],
    [
        "Corneal Ulcer (Keratitis)",
        "eye pain, redness, excessive watering, discharge, blurred vision, sensitivity to light, feeling of something in eye, white spot on cornea",
        "This is urgent - Triphala wash only after doctor advice; Rose water protection after healing",
        "Antibacterial / antifungal eye drops every hour (Moxifloxacin ₹80 Rs, Natamycin ₹200 Rs); cycloplegics; urgent ophthalmology",
        "Seek urgent ophthalmologist care. Never wear contact lenses while sleeping. Maintain lens hygiene. Avoid rubbing eyes.",
        "Ophthalmologist"
    ],

    # ─────────────────────────── Skin / dermatology ───────────────────────────
    [
        "Contact Dermatitis",
        "red rash at the contact site, itching, burning, dry cracked skin, blisters, swelling, oozing, tenderness",
        "Neem paste (₹35 Rs) - Soothes the skin; Aloe vera gel (₹40 Rs) - Cooling; Turmeric paste (₹40 Rs) - Anti-inflammatory",
        "Hydrocortisone cream (₹35 Rs) - Reduces inflammation; antihistamines (Cetirizine ₹20 Rs); avoid the allergen",
        "Identify and avoid the triggering substance. Apply cool compresses. Wash the area with mild soap. Use gloves with chemicals.",
        "Dermatologist"
    ],
    [
        "Seborrheic Dermatitis (Dandruff)",
        "flaky dandruff, oily scaly patches on scalp, itching, redness, flakes on eyebrows and sides of nose, cradle cap in infants",
        "Neem scalp oil (₹50 Rs) - Antifungal; Reetha (soapnut) wash (₹40 Rs) - Cleanses scalp; Aloe vera scalp mask (₹40 Rs)",
        "Ketoconazole shampoo (₹80 Rs) - Antifungal; selenium sulfide shampoo; steroid lotion for flares",
        "Wash hair regularly with medicated shampoo. Avoid harsh styling products. Manage stress. Don't scratch and pick flakes.",
        "Dermatologist"
    ],
    [
        "Rosacea",
        "persistent facial redness, visible blood vessels, red bumps and pimples, eye irritation and dryness, thickened skin, flushing with triggers",
        "Aloe vera gel (₹40 Rs) - Calms redness; Neem face pack (₹35 Rs) - Antibacterial; cooling cucumber mask (₹30 Rs)",
        "Metronidazole gel (₹100 Rs) - Topical; doxycycline (₹90 Rs) - Oral; laser for redness",
        "Protect skin with sunscreen daily. Avoid spicy foods, alcohol and heat. Use gentle cleansers. Track your trigger factors.",
        "Dermatologist"
    ],
    [
        "Vitiligo",
        "white patches of skin on face, hands, knees, symmetrical patches, premature greying of hair, depigmentation around mouth and eyes",
        "Bakuchi oil (₹70 Rs) - Repigmentation; Manjistha (₹80 Rs) - Blood purifier; Neem capsules (₹60 Rs) - Immune balance",
        "Topical corticosteroids; phototherapy (NB-UVB ₹200 Rs); tacrolimus ointment; skin grafting in selective cases",
        "Prevent sunburn on patches with sunscreen. Consider phototherapy consistently. Camouflage with makeup if desired. Psychological support helps.",
        "Dermatologist"
    ],
    [
        "Alopecia Areata",
        "sudden round patches of hair loss on scalp, hair loss in other body areas, patchy bald spots, itching or tingling before patches, changes in nails",
        "Bhringraj oil (₹70 Rs) - Hair growth; Amla and reetha wash (₹40 Rs) - Scalp health; Ashwagandha (₹120 Rs) - Stress reduction",
        "Minoxidil (₹50 Rs) - Hair growth; intralesional steroid injections; contact immunotherapy for extensive loss",
        "Manage stress which often triggers it. Use prescribed treatments regularly. Gentle hair care. Most patches regrow spontaneously.",
        "Dermatologist"
    ],
    [
        "Urticaria (Hives)",
        "raised itchy welts on skin, red or skin-colored bumps, swelling that comes and goes, burning or stinging, welts lasting hours",
        "Neem paste (₹35 Rs) - Soothes; Cooling aloe vera gel (₹40 Rs); Coriander and fennel cooling drink (₹30 Rs)",
        "Antihistamines (Cetirizine ₹20 Rs, Fexofenadine ₹30 Rs); steroid short course for severe; identify triggers",
        "Identify and avoid triggers (foods, stress, heat). Take antihistamines as prescribed. Cool baths reduce itching. Seek care for swelling of lips or breathing difficulty.",
        "Dermatologist / Allergist"
    ],
    [
        "Boil (Furuncle)",
        "painful red swollen lump under skin, growing tender over days, white or yellow center, pus drainage, fever, redness around boil",
        "Neem and turmeric paste (₹35 Rs) - Draws out infection; warm Triphala compress (₹30 Rs); Guduchi (₹60 Rs) - Immune support",
        "Warm compresses; incision and drainage by a doctor; antibiotics (Cloxacillin ₹50 Rs) if infection spreads",
        "Apply warm compresses to encourage drainage. Never squeeze - let a doctor drain it. Keep the area clean. Recurrent boils need evaluation.",
        "Dermatologist / General Physician"
    ],
    [
        "Athlete's Foot (Tinea Pedis)",
        "itchy scaly rash between toes, peeling cracked skin, burning and stinging, blisters, raw skin, foul smell, thickened toenails",
        "Neem oil (₹50 Rs) - Antifungal; tea tree oil application (₹70 Rs); keep feet dry with Triphala dusting powder (₹30 Rs)",
        "Terbinafine cream (₹90 Rs) - Antifungal; Clotrimazole powder; oral terbinafine for stubborn cases",
        "Keep feet clean and dry, especially between toes. Wear breathable footwear. Change socks daily. Don't walk barefoot in public showers.",
        "Dermatologist"
    ],
    [
        "Impetigo",
        "red sores that rupture and ooze, honey-colored crusts, blisters on face and limbs, itchy sores, sores spreading to other areas, swollen lymph nodes",
        "Neem and turmeric paste (₹35 Rs) - Antibacterial; Manjistha (₹80 Rs) - Blood purifier; gentle Triphala wash (₹30 Rs)",
        "Topical mupirocin (₹90 Rs) - Antibacterial; oral antibiotics (Cephalexin ₹60 Rs) for extensive cases",
        "Wash sores gently and cover them. Complete antibiotics. Wash hands frequently. Don't share towels. Keep nails short to prevent spread.",
        "Dermatologist / Pediatrician"
    ],
    [
        "Warts",
        "small rough raised bumps on skin, flesh-colored warts on hands and feet, black dots in wart, warts on soles painful while walking, cauliflower-like surface",
        "Neem paste (₹35 Rs) - Antiviral; garlic application (₹40 Rs) - Viral wart remedy; Kshara application by specialist",
        "Salicylic acid topical (₹60 Rs) - Peels the wart; cryotherapy (freezing); immunotherapy for stubborn warts",
        "Apply wart treatment consistently. Don't pick at warts. Wash hands after touching. Cover warts to prevent spread. See a doctor if persistent.",
        "Dermatologist"
    ],

    # ─────────────────────────── Musculoskeletal / rheumatology ───────────────────────────
    [
        "Osteoarthritis",
        "joint pain worsens with activity, morning stiffness under 30 minutes, grinding sensation in joint, swelling, reduced flexibility, bone spurs",
        "Shallaki (Boswellia) (₹110 Rs) - Anti-inflammatory; Guggulu (₹90 Rs) - Joint health; Mahanarayan oil massage (₹130 Rs)",
        "Paracetamol (₹15 Rs) - Pain relief; topical NSAIDs; hyaluronic acid injections; joint replacement in severe cases",
        "Exercise with low-impact activities. Maintain a healthy weight. Use hot/cold therapy. Supportive footwear and canes reduce strain.",
        "Rheumatologist / Orthopedic Surgeon"
    ],
    [
        "Rheumatoid Arthritis",
        "painful swollen joints on both sides, morning stiffness over an hour, fatigue, fever, weight loss, lumps under skin (rheumatoid nodules), dry eyes",
        "Shallaki (₹110 Rs) - Anti-inflammatory; Guggulu (₹90 Rs) - Joint relief; Ashwagandha (₹120 Rs) - Immune balance",
        "Methotrexate (₹80 Rs) - DMARD; hydroxychloroquine (₹50 Rs); biologics for severe disease; steroids short-term",
        "Start DMARDs early to prevent joint damage. Do gentle range-of-motion exercises. Balanced diet with omega-3s. Regular rheumatology follow-up.",
        "Rheumatologist"
    ],
    [
        "Fibromyalgia",
        "widespread muscle pain, fatigue, sleep problems, brain fog, tender points, headaches, irritable bowel symptoms, stiffness, sensitivity to pain",
        "Ashwagandha (₹120 Rs) - Pain and fatigue; Brahmi (₹90 Rs) - Brain fog; warm Dashamoola oil massage (₹100 Rs)",
        "Pregabalin (₹70 Rs) - Pain; duloxetine (₹90 Rs) - Pain and mood; graded exercise and CBT",
        "Pace your activities and avoid overexertion. Gentle exercise like yoga and walking. Good sleep hygiene. Cognitive behavioral therapy helps.",
        "Rheumatologist / Pain Specialist"
    ],
    [
        "Frozen Shoulder (Adhesive Capsulitis)",
        "stiffness and pain in one shoulder, limited range of motion, pain worse at night, difficulty with daily tasks, frozen then thawing phases",
        "Mahanarayan oil massage (₹130 Rs) - Shoulder mobility; Dashamoola (₹90 Rs) - Anti-inflammatory; warm compresses",
        "NSAIDs (Diclofenac ₹25 Rs) - Pain relief; physiotherapy; intra-articular steroid injections",
        "Do daily stretching exercises as guided. Heat before exercise, ice after. Keep moving the shoulder gently. Physiotherapy is key.",
        "Orthopedic Surgeon / Physiotherapist"
    ],
    [
        "Tennis Elbow (Lateral Epicondylitis)",
        "pain on the outer elbow, pain worsens with gripping or lifting, tenderness over the elbow bone, weak grip, pain radiating to forearm",
        "Nirgundi oil massage (₹100 Rs) - Local relief; Shallaki (₹110 Rs) - Anti-inflammatory; Turmeric paste compress (₹40 Rs)",
        "NSAID gels (Diclofenac ₹80 Rs); physiotherapy; steroid injections; rarely surgery",
        "Rest the affected arm. Use a counterforce strap. Apply ice and do stretching. Modify your grip and lifting technique.",
        "Orthopedic Surgeon / Physiotherapist"
    ],
    [
        "Plantar Fasciitis",
        "sharp heel pain with first steps in the morning, pain after long standing, heel tenderness, pain with stretching the foot, burning in sole",
        "Warm oil foot massage with Nirgundi (₹100 Rs) - Soothing; Turmeric foot soak (₹40 Rs); Dashamoola (₹90 Rs) - Anti-inflammatory",
        "Supportive footwear and orthotics; NSAIDs (Ibuprofen ₹25 Rs); plantar fascia stretching; shockwave therapy",
        "Stretch the calf and plantar fascia every morning. Wear cushioned shoes. Ice the heel after activity. Avoid walking barefoot on hard floors.",
        "Orthopedic Surgeon / Physiotherapist"
    ],
    [
        "Ankylosing Spondylitis",
        "lower back pain and stiffness worse in the morning and with rest, improves with exercise, pain in buttocks, reduced flexibility, fatigue, eye inflammation",
        "Shallaki (₹110 Rs) - Anti-inflammatory; Guggulu (₹90 Rs) - Joint health; Dahmamoola (₹90 Rs) - Back support",
        "NSAIDs (Naproxen ₹30 Rs); biologics (Sulfasalazine ₹70 Rs, TNF inhibitors); physiotherapy",
        "Exercise daily - posture and stretching is vital. Sleep on a firm bed. Avoid prolonged sitting. Quit smoking. Regular rheumatology care.",
        "Rheumatologist"
    ],

    # ─────────────────────────── Dental / oral ───────────────────────────
    [
        "Tooth Decay (Dental Caries)",
        "toothache, sensitivity to hot cold and sweet, visible holes in teeth, pain on biting, white or brown spots on teeth, bad taste",
        "Clove oil application (₹40 Rs) - Pain relief; Triphala mouth rinse (₹50 Rs) - Antiseptic; Licorice mouth rinse (₹40 Rs)",
        "Fluoride treatment; dental fillings; root canal for deep decay; extraction for unsalvageable teeth",
        "Brush twice daily with fluoride toothpaste. Limit sugary snacks. Floss daily. Visit the dentist every 6 months.",
        "Dentist"
    ],
    [
        "Gingivitis",
        "bleeding gums while brushing, red swollen gums, bad breath, tender gums, receding gums, gum tenderness",
        "Triphala powder rinse (₹50 Rs) - Antiseptic; Aloe vera gum massage (₹40 Rs); Neem stick brushing (₹30 Rs)",
        "Professional cleaning (scaling); improved oral hygiene; medicated mouthwash (Chlorhexidine ₹60 Rs)",
        "Brush and floss properly twice daily. Use an antiseptic mouthwash. Get professional scaling. Stop smoking which worsens gum disease.",
        "Dentist"
    ],
    [
        "Periodontitis",
        "bad breath, receding gums, loose teeth, painful chewing, red bleeding swollen gums, pus between teeth, change in bite",
        "Triphala mouth rinse (₹50 Rs) - Reduces gum inflammation; Neem and honey gum paste (₹35 Rs); Aloe vera massage (₹40 Rs)",
        "Deep cleaning (scaling and root planing); antibiotics (Amoxicillin ₹50 Rs); surgery for advanced cases",
        "Commit to excellent oral hygiene. Professional deep cleaning. Quit smoking. Regular dental check-ups every 3-6 months.",
        "Dentist (Periodontist)"
    ],
    [
        "Tooth Abscess",
        "severe throbbing toothache, pain radiating to jaw and ear, fever, swollen face or cheek, sensitivity to hot and cold, swollen gum, bad taste",
        "Clove oil (₹40 Rs) - Pain relief; warm Triphala salt water rinse (₹30 Rs); Guduchi (₹60 Rs) - Infection support",
        "Antibiotics (Amoxicillin ₹50 Rs); root canal or extraction; incision and drainage of the abscess",
        "See a dentist immediately. Take prescribed antibiotics. Rinse with warm salt water. Pain relief for comfort.",
        "Dentist / Emergency Dental"
    ],
    [
        "Canker Sore (Aphthous Ulcer)",
        "painful round shallow ulcers inside mouth, pain worse when eating or talking, burning sensation, white or yellow center with red border, recurrent sores",
        "Triphala mouth rinse (₹50 Rs) - Heals ulcers; Honey application (₹40 Rs) - Soothing; Yashtimadhu (₹80 Rs) - Reduces sores",
        "Topical anesthetic gels (Lignocaine ₹50 Rs); steroid mouthwashes; avoid triggers",
        "Avoid spicy, acidic and hard foods during outbreaks. Use a soft toothbrush. Manage stress. Rinse with warm salt water.",
        "Dentist / General Physician"
    ],
    [
        "TMJ Disorder (Temporomandibular Joint)",
        "jaw pain or tenderness, pain in temple and ear, clicking or popping sounds on jaw movement, difficulty opening the mouth fully, facial pain, locking of jaw",
        "Mahanarayan oil jaw massage (₹130 Rs) - Relaxes muscles; Dashamoola (₹90 Rs) - Anti-inflammatory; warm compress (₹20 Rs)",
        "NSAIDs (Ibuprofen ₹25 Rs); muscle relaxants; mouth guards for grinding; physiotherapy",
        "Eat soft foods and avoid wide mouth opening. Use warm compresses and gentle jaw exercises. Manage teeth grinding with a mouthguard.",
        "Dentist / Maxillofacial Specialist"
    ],

    # ─────────────────────────── Women's health / gynaecology ───────────────────────────
    [
        "Dysmenorrhea (Menstrual Cramps)",
        "cramping pain in lower abdomen during periods, pain radiating to back and thighs, nausea, diarrhea, headache, dizziness, fatigue",
        "Ashwagandha (₹120 Rs) - Antispasmodic; warm Dashamoola oil massage on lower belly (₹100 Rs); ginger turmeric tea (₹40 Rs)",
        "Ibuprofen (₹25 Rs) - Pain relief; naproxen for cramps; hormonal birth control if needed",
        "Apply a heating pad to the lower abdomen. Gentle exercise and stretching. Warm baths. Rest and hydration. See a gynaecologist for severe pain.",
        "Gynaecologist / General Physician"
    ],
    [
        "Menopause Syndrome",
        "hot flashes, night sweats, irregular periods, mood swings, vaginal dryness, sleep problems, fatigue, weight gain, reduced libido",
        "Shatavari (₹90 Rs) - Hormonal balance; Ashwagandha (₹120 Rs) - Manages stress; black cohosh-like cooling herbs",
        "Hormone replacement therapy (HRT) when appropriate; vaginal moisturizers; antidepressants for hot flashes in some",
        "Exercise and a balanced diet rich in calcium and vitamin D. Manage stress with relaxation. Limit caffeine and spicy foods. Discuss HRT benefits with a doctor.",
        "Gynaecologist"
    ],
    [
        "Endometriosis",
        "severe pelvic pain, painful periods, pain during intercourse, heavy bleeding, pain with urination or bowel movements, difficulty conceiving, fatigue",
        "Shatavari (₹90 Rs) - Hormone balance; Dashamoola (₹90 Rs) - Anti-inflammatory; Ashwagandha (₹120 Rs) - Pain support",
        "NSAIDs (₹25 Rs) - Pain; hormonal therapy (combined pills, GnRH agonists); laparoscopy surgery",
        "Manage pain with prescribed treatment. Gentle exercise and pelvic physiotherapy. Follow dietary anti-inflammatory choices. Fertility planning with specialist.",
        "Gynaecologist"
    ],
    [
        "Vaginal Candidiasis (Yeast Infection)",
        "itching and soreness around the vagina, thick white cottage-cheese discharge, burning during urination, pain during intercourse, redness and swelling",
        "Neem wash (₹35 Rs) - Antifungal; curd (probiotic) application under guidance; Haridra (Turmeric) (₹40 Rs) - Internal use",
        "Clotrimazole vaginal cream (₹100 Rs) - Antifungal; fluconazole oral tablet (₹70 Rs)",
        "Keep the area clean and dry. Wear cotton underwear. Avoid scented products. Complete the antifungal treatment. See a gynaecologist for recurrent infection.",
        "Gynaecologist"
    ],
    [
        "Premenstrual Syndrome (PMS)",
        "mood swings, irritability, bloating, breast tenderness, fatigue, food cravings, headache, sleep problems, breast swelling, concentration difficulty",
        "Shatavari (₹90 Rs) - Hormone balance; Ashwagandha (₹120 Rs) - Mood support; ginger tea for bloating (₹40 Rs)",
        "SSRIs for severe mood symptoms; NSAIDs for cramps; calcium and vitamin B6 supplements",
        "Exercise regularly and reduce salt and caffeine around periods. Eat smaller frequent meals. Manage stress. Track symptoms to predict them.",
        "Gynaecologist / General Physician"
    ],

    # ─────────────────────────── Urgent / emergency ───────────────────────────
    [
        "Heat Stroke",
        "high body temperature (above 104F), hot dry skin, confusion, rapid heartbeat, rapid shallow breathing, nausea, vomiting, seizures, fainting",
        "This is an emergency - Cool the body fast (cold water, ice packs), later Amalaki (₹50 Rs) - Rehydration support",
        "Emergency: rapid cooling in hospital, IV fluids, monitoring of organ function",
        "Call emergency services immediately. Move to shade and cool rapidly with cold water. Give sips of water if conscious. Never wait it out.",
        "Emergency Medicine"
    ],
    [
        "Dehydration",
        "extreme thirst, dry mouth and lips, dark yellow urine, infrequent urination, dizziness, fatigue, sunken eyes, headache, rapid heartbeat, confusion",
        "Coconut water (₹20 Rs) - Natural electrolyte; Coriander seed water (₹20 Rs); warm Triphala water",
        "Oral rehydration salts (ORS ₹20 Rs); IV fluids for severe cases; treat underlying cause",
        "Drink fluids and ORS gradually. Avoid caffeine and alcohol. Monitor urine color. Seek care for confusion, weakness or inability to keep fluids down.",
        "General Physician / Emergency Medicine"
    ],
]

def main():
    wb = openpyxl.load_workbook(FILE)
    ws = wb.active

    existing = set()
    for row in ws.iter_rows(min_row=2, values_only=True):
        name = str(row[0]).strip().lower() if row and row[0] else ""
        if name:
            existing.add(name)

    added = 0
    for row in EXPANSION:
        name = str(row[0]).strip().lower()
        if not name or name in existing:
            print(f"  - Skip (already present): {row[0]}")
            continue
        ws.append(row)
        existing.add(name)
        added += 1

    wb.save(FILE)
    total = ws.max_row - 1
    print(f"\nDone. Added {added} new diseases.")
    print(f"Total diseases in dataset now: {total}")


if __name__ == "__main__":
    main()