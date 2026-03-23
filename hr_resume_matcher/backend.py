from fastapi import FastAPI, Form
from pydantic import BaseModel
from core import calculate_match_score, generate_feedback_email

app = FastAPI(title="HR Resume Matcher API")

class MatchResponse(BaseModel):
    candidate_name: str
    match_score: float
    feedback_email: str

@app.post("/evaluate_candidate", response_model=MatchResponse)
async def evaluate_candidate(
    candidate_name: str = Form(...),
    resume_text: str = Form(...),
    jd_text: str = Form(...)
):
    # 1. Calculate ML Score
    score = calculate_match_score(resume_text, jd_text)
    
    # 2. Generate GenAI Feedback
    email = generate_feedback_email(candidate_name, resume_text, jd_text, score)
    
    return {
        "candidate_name": candidate_name,
        "match_score": score,
        "feedback_email": email
    }

