from src.resume_parser import parse_resume

if __name__ == "__main__":
    result = parse_resume("data/resume/resume (1).pdf")
    print(result)
