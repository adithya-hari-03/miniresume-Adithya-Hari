from pymongo import MongoClient
from bson import ObjectId
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date
import uuid
import os

app = FastAPI(title="Mini Resume Management API")

client = MongoClient("mongodb://localhost:27017")
db = client["resume_database"]
collection = db["candidates"]
# In-memory storage


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


class CandidateResponse(BaseModel):
    id: str
    full_name: str
    dob: date
    contact_number: str
    contact_address: str
    education_qualification: str
    graduation_year: int
    years_of_experience: float
    skill_set: List[str]
    resume_filename: str

@app.get("/")
def root():
    return {"message": "Mini Resume Management API is running"}


@app.get("/health", status_code=200)
def health_check():
    return {"status": "healthy"}


@app.post("/candidates", response_model=CandidateResponse, status_code=201)
async def create_candidate(
    full_name: str = Form(...),
    dob: date = Form(...),
    contact_number: str = Form(...),
    contact_address: str = Form(...),
    education_qualification: str = Form(...),
    graduation_year: int = Form(...),
    years_of_experience: float = Form(...),
    skill_set: str = Form(...),
    resume: UploadFile = File(...)
):
    # Validate file type
    if not resume.filename.endswith((".pdf", ".doc", ".docx")):
        raise HTTPException(status_code=400, detail="Invalid file type")

    candidate_id = str(uuid.uuid4())

    file_path = os.path.join(UPLOAD_FOLDER, f"{candidate_id}_{resume.filename}")

    with open(file_path, "wb") as buffer:
        content = await resume.read()
        buffer.write(content)

    candidate_data = {
        "id": candidate_id,
        "full_name": full_name,
        "dob": dob.isoformat(),
        "contact_number": contact_number,
        "contact_address": contact_address,
        "education_qualification": education_qualification,
        "graduation_year": graduation_year,
        "years_of_experience": years_of_experience,
        "skill_set": [skill.strip().lower() for skill in skill_set.split(",")],
        "resume_filename": f"{candidate_id}_{resume.filename}"
    }


    collection.insert_one(candidate_data)

    return candidate_data


@app.get("/candidates", response_model=List[CandidateResponse])
def list_candidates(
    skill: Optional[str] = Query(None),
    experience: Optional[float] = Query(None),
    graduation_year: Optional[int] = Query(None)
):
    results = list(collection.find({}, {"_id": 0}))

    if skill:
        results = [
            c for c in results
            if skill.lower() in c["skill_set"]
        ]

    if experience is not None:
        results = [
            c for c in results
            if c["years_of_experience"] >= experience
        ]

    if graduation_year is not None:
        results = [
            c for c in results
            if c["graduation_year"] == graduation_year
        ]

    return results


@app.get("/candidates/{candidate_id}", response_model=CandidateResponse)
def get_candidate(candidate_id: str):

    candidate = collection.find_one({"id": candidate_id})

    if candidate:

        return candidate

    raise HTTPException(status_code=404, detail="Candidate not found")


@app.delete("/candidates/{candidate_id}", status_code=200)
def delete_candidate(candidate_id: str):

    result = collection.delete_one({"id": candidate_id})

    if result.deleted_count == 1:
        return {"message": "Candidate deleted successfully"}

    raise HTTPException(status_code=404, detail="Candidate not found")
