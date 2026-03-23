  HR Resume Matcher & GenAI Feedback Generator

[![Streamlit App](https://static.streamlit.io/badges/featured.svg)](https://your-streamlit-link.streamlit.app)
[![FastAPI Backend](https://img.shields.io/badge/FastAPI-Backend-blue)](http://127.0.0.1:8000/docs)

  Features
- **📊 ML Matching**: TF-IDF cosine similarity (resume vs JD)
- **🤖 GenAI Feedback**: Gemini extracts **matching skills**, **skills to improve**, **job fit (Yes/No)**, **HR email**
- **📤 File Upload**: PDF/DOCX resumes + JDs
- **✨ Live Demo**: [Try it](https://your-streamlit-link.streamlit.app)

##  Screenshots
**Dashboard**  
![Dashboard](screenshots/dashboard.png)

**Results** (Score + Skills + Email)  
![Results](screenshots/results.png)

**API Docs**  
![API](screenshots/api.png)

##  Structure
```
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
```

##  Quick Start (Local)
```bash
pip install -r requirements.txt
cd hr_resume_matcher
uvicorn backend:app --reload  # http://127.0.0.1:8000/docs
streamlit run frontend.py     # http://localhost:8502
```

**Add your GEMINI_API_KEY to .env**

## ☁️ Deploy (Streamlit Cloud)
1. Push to GitHub
2. [Streamlit Cloud](https://share.streamlit.io) → New app → `frontend.py`
3. Backend: Render.com (Docker)

## 📦 Dependencies
```
fastapi uvicorn streamlit scikit-learn google-generativeai python-dotenv PyPDF2 python-docx python-multipart
```

## 🎖️ Tech Stack
- **ML**: scikit-learn (TF-IDF)
- **AI**: Google Gemini 2.0 Flash
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Files**: PyPDF2, docx

**Live Demo**: [Demo Link](https://your-streamlit-link.streamlit.app)  
**Repo**: [GitHub](https://github.com/viveksalimath)

**📈 Portfolio Project** – Open Source HR Tech!

