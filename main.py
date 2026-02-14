from fastapi import FastAPI, status
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI(title="Mini Resume Collector API")

# In-memory storage
resumes: List["Resume"] = []

class Resume(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    skills: List[str]
    experience: int

@app.get("/")
def root():
    return {"message": "Mini Resume Collector API is running"}

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "healthy"}

@app.post("/resumes", status_code=status.HTTP_201_CREATED)
def create_resume(resume: Resume):
    resumes.append(resume)
    return {
        "message": "Resume submitted successfully",
        "data": resume
    }

@app.get("/resumes", response_model=List[Resume])
def get_resumes():
    return resumes
