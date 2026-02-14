# Mini Resume Management API

## Objective

This project implements a REST API using FastAPI that allows:

- Uploading resumes (PDF/DOC/DOCX)
- Storing candidate metadata
- Categorizing candidates by skills and experience
- Filtering/searching candidates
- Fetching candidate by ID
- Deleting candidate

---

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn

---

## Project Structure

miniresume-Adithya Hari/
│
├── main.py  
├── requirements.txt  
├── README.md  
└── uploads/ (created automatically when uploading resumes)

---

## Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/adithya-hari-03/miniresume-Adithya-Hari.git
cd miniresume-Adithya-Hari
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**
```bash
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### 1. Health Check

**GET /health**

Response:

```json
{
  "status": "healthy"
}
```

---

### 2. Create Candidate

**POST /candidates**

Form Data Fields:

- full_name  
- dob (YYYY-MM-DD)  
- contact_number  
- contact_address  
- education_qualification  
- graduation_year  
- years_of_experience  
- skill_set (comma-separated values)  
- resume (PDF/DOC/DOCX file upload)  

Success Response: **201 Created**

Example skill_set:

```
python, fastapi, sql
```

---

### 3. List Candidates

**GET /candidates**

Optional Query Parameters:

- skill  
- experience  
- graduation_year  

Example:

```
/candidates?skill=python&experience=2
```

---

### 4. Get Candidate by ID

**GET /candidates/{id}**

Returns candidate details.

---

### 5. Delete Candidate

**DELETE /candidates/{id}**

Response:

```json
{
  "message": "Candidate deleted successfully"
}
```

---

## Notes

- Data is stored in memory (no database required).
- Uploaded resumes are stored inside the `uploads/` folder.
- Only PDF, DOC, and DOCX file types are allowed.



