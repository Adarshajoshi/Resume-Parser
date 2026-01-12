import spacy
from spacy.matcher import PhraseMatcher
from rake_nltk import Rake

nlp=spacy.load("en_core_web_sm")

def load_skills(path="data/skills/skills.txt"):
    skills={}
    with open(path,"r") as f:
        for line in f:
            variants=line.strip().split("|")
            for v in variants:
                skills[v.strip().lower()]=True
        return skills
    
def extract_skills(text: str):
    skills = load_skills()
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    patterns = [nlp(skill) for skill in skills]
    matcher.add("SKILLS", patterns)

    doc = nlp(text)
    matches = matcher(doc)

    return list(set([doc[start:end].text for _, start, end in matches]))