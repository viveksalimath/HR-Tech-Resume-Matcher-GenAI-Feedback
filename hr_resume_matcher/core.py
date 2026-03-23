import os
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

load_dotenv()

# Gemini API Key from .env
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file. Please add it and restart.")
genai.configure(api_key=api_key)

def calculate_match_score(resume_text: str, jd_text: str) -> float:
    """TF-IDF similarity score."""
    if not resume_text or not jd_text:
        return 0.0
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(similarity * 100, 2)

def generate_feedback_email(candidate_name: str, resume_text: str, jd_text: str, score: float) -> str:
    """Gemini analysis + HR email with matches/improvements."""
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config={
            "temperature": 0.7,
            "top_k": 1,
            "top_p": 1,
            "max_output_tokens": 2048,
        },
        safety_settings={
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        }
    )
    
    prompt = f"""Analyze resume vs JD for '{candidate_name}' (match score: {score}%).

**JD Excerpt:** {jd_text[:2000]}
**Resume Excerpt:** {resume_text[:2000]}

Respond EXACTLY in Markdown format:

**📊 MATCHING SKILLS (top 4-6):**
• Skill 1 from resume matching JD
• Skill 2...

**🔧 SKILLS TO IMPROVE (top 4-6 gaps from JD):**
• Missing skill 1
• Missing skill 2...

**✅ JOB FIT:** Yes/No  
*(1-sentence reason based on score + skills)*

**✉️ HR RECRUITER EMAIL:**  
Full professional email (empathetic, concise):  
- >70%: Advance to interview + highlights  
- <70%: Polite decline + improvement tips  

No extra text."""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"""**AI Error:** {str(e)}  
Score: {score}% - Review manually.
**Fallback:** Check resume vs JD for Python/ML skills match."""

