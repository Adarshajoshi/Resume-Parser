import spacy

nlp=spacy.load("en_core_web_sm")

def extract_experience(text: str):
    doc = nlp(text)
    experience = []

    for ent in doc.ents:
        if ent.label_ == "ORG":
            experience.append(ent.text)

    return list(set(experience))
