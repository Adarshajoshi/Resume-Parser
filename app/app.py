import sys
import os

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from src.resume_parser import parse_resume

st.set_page_config(page_title="Resume Parser", layout="centered")

st.title("📄 Resume Parser")

uploaded_file = st.file_uploader("Upload a resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Parsing resume..."):
        result = parse_resume("temp.pdf")

    st.success("Parsed successfully!")
    st.json(result)
