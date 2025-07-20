Resume Scanner 
An intelligent resume analyzer that extracts information and scores resumes against job descriptions using NLP.
Features:
- Upload resumes (PDF, DOCX)
- Extracts key data: name, email, education, skills, experience
- Matches resume against job descriptions (JD)
- Scores based on keyword overlap and skill relevance
- Provides feedback on missing skills or keywords
Tech Stack:
- Python
- spaCy / nltk for NLP
- pdfminer / docx2txt for file parsing
- Streamlit or Flask (UI)
- scikit-learn (optional for scoring model)
Folder Structure:
```
resume-scanner/
├── app/
│   ├── main.py              # UI + logic
│   ├── parser.py            # Resume parsing functions
│   ├── matcher.py           # JD matching logic
│   ├── utils.py             # Helper functions
├── data/
│   ├── resumes/             # Sample resumes
│   ├── job_descriptions/    # Job description examples
├── requirements.txt
└── README.md
```
Setup:
1.Install dependencies
```bash
pip install -r requirements.txt
```
2.Run the app
If using Streamlit:
```bash
streamlit run app/main.py
```
If using Flask:
```bash
python app/main.py
```
3.Upload a resume- Compare it with a sample job description
- See a match score and suggested improvements
Future Improvements:
- GPT-powered feedback and resume rewrite
- Named Entity Recognition (NER) for more accuracy
- PDF report export with score summary
- Applicant tracking system (ATS) integration
License:
MIT
