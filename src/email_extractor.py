import re

def extract_email(text: str):
    pattern=r"[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    match=re.search(pattern,text)
    return match.group() if match else None