from src.pdf_extractor import extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.email_extractor import extract_email
from src.ner_extractor import extract_name, extract_university

def parse_resume(pdf_path: str):
    text = extract_text_from_pdf(pdf_path)

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "skills": extract_skills(text),
        "university": extract_university(text)
    }
