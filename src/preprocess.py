import re

def clean_text(text: str) -> str:
    text = text.replace("■", " ")
    text = re.sub(r'\s+', ' ', text)
    text = text.replace("|", " ")
    return text.strip()

def split_sections(text: str):
    sections = {}
    current = "OTHER"

    for line in text.split("\n"):
        lower = line.lower()

        if "education" in lower:
            current = "EDUCATION"
        elif "skill" in lower:
            current = "SKILLS"
        elif "project" in lower:
            current = "PROJECTS"
        elif "experience" in lower:
            current = "EXPERIENCE"

        sections.setdefault(current, []).append(line)

    return sections
