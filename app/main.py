import streamlit as st
from resume_parser import extract_text_from_pdf
from job_matcher import match_resume_to_jd

st.title("📄 Resume Scanner using NLP")
st.write("Upload a resume and a job description to see how well they match.")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description", height=200)

if resume_file and job_description:
    resume_text = extract_text_from_pdf(resume_file)
    score = match_resume_to_jd(resume_text, job_description)
    st.success(f"Match Score: {score:.2f}%")
