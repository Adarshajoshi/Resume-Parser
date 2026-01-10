README.md (Starter Version)
# Resume Parser (NLP)

An NLP-based resume parser that extracts structured information from PDF resumes using spaCy and rule-based matching.

## Features
- Extracts candidate name
- Extracts email address
- Identifies skills using PhraseMatcher
- Detects universities using Named Entity Recognition

## Tech Stack
- Python
- spaCy
- PyPDF / pdfplumber
- Regex

## Project Structure


resume-parser/
├── data/
├── src/
├── main.py
└── README.md


## How to Run
```bash
git clone https://github.com/Adarshajoshi/resume-parser.git
cd resume-parser
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main"# Resume-Parser" 
