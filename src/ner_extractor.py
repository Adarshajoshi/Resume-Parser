import spacy

nlp=spacy.load("en_core_web_sm")

def extract_name(text: str):
    doc=nlp(text)
    for ent in doc.ents:
        if ent.label_=="PERSON":
            return ent.text
        return None
    
def extract_university(text: str):
    doc=nlp(text)
    keywords=["University","College","Institute","School"]
    universities=[]

    for ent in doc.ents:
        if ent.label_=="ORG" and any(k in ent.text for k in keywords):
            universities.append(ent.text)
        
    return list(set(universities))