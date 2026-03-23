# 📄 HR Resume Matcher & GenAI Feedback Generator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-link.streamlit.app)
[![FastAPI Backend](https://img.shields.io/badge/FastAPI-Backend-blue.svg)](http://127.0.0.1:8000/docs)

An open-source HR Tech portfolio project that combines Machine Learning and Generative AI to evaluate resumes against job descriptions. It provides ATS matching scores and actionable AI-driven feedback to help candidates optimize their applications.

**[✨ Live Demo](https://your-streamlit-link.streamlit.app)** | **[🐙 GitHub Repo](https://github.com/viveksalimath/your-repo-name)**

---

## ✨ Features

- **📊 ML Matching:** Calculates TF-IDF cosine similarity between the resume and the Job Description (JD).
- **🤖 GenAI Feedback:** Leverages Google Gemini 2.0 Flash to extract matching skills, identify missing skills, determine overall job fit (Yes/No), and draft an HR email.
- **📤 Multi-Format Uploads:** Supports parsing for both PDF and DOCX resume formats.
- **⚡ Interactive UI & API:** Built with a Streamlit frontend and a FastAPI backend.

---

## 📸 Screenshots

| Streamlit Dashboard | FastAPI Docs |
| :---: | :---: |
| ![Dashboard](screenshots/dashboard.jpg) | ![API Docs](screenshots/api_docs.jpg) |

---

## 📂 Project Structure

```text
HR Tech Resume Matcher & GenAI Feedback/
├── hr_resume_matcher/
│   ├── core.py          # TF-IDF + Gemini logic
│   ├── backend.py       # FastAPI /evaluate_candidate
│   ├── frontend.py      # Streamlit UI + uploads
│   ├── .env             # GEMINI_API_KEY
│   └── .gitignore
├── requirements.txt     # Dependencies
├── README.md
└── TODO.md
