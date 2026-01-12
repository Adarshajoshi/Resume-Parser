import spacy

nlp=spacy.load("en_core_web_sm")

def extract_name(text: str):
    lines = text.split("\n")[:5]

    # Heuristic: ALL CAPS line with 2–3 words
    for line in lines:
        if line.isupper() and 1 < len(line.split()) <= 3:
            return line.title()

    doc = nlp(" ".join(lines))
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return None

def extract_university(text: str):
    doc=nlp(text)
    keywords=["University","College","Institute","School","Campus"]
    universities=[]

    for ent in doc.ents:
        if ent.label_=="ORG" and any(k in ent.text for k in keywords):
            universities.append(ent.text)
        
    return list(set(universities))