# Mini Resume Management API

## Objective

This project implements a REST API using FastAPI that allows:

- Uploading resumes (PDF/DOC/DOCX)
- Storing candidate metadata
- Persisting candidate data in MongoDB database
- Categorizing candidates by skills and experience
- Filtering/searching candidates
- Fetching candidate by ID
- Deleting candidate

---

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- MongoDB
- PyMongo

---

## Project Structure

miniresume-Adithya-Hari/
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

---

### 2. Create a virtual environment

```bash
python -m venv .venv
```

---

### 3. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Ensure MongoDB is running

The application uses a local MongoDB instance:

```
mongodb://localhost:27017
```

Database used:

```
resume_database
```

Collection:

```
candidates
```

You can verify data using **MongoDB Compass**.

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
python, fastapi, mongodb
```

Uploaded resume files are stored in the `uploads/` folder.

Candidate metadata is stored in **MongoDB**.

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

Returns candidate details stored in the database.

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

## Data Persistence

Candidate data is stored in **MongoDB**.

Each submission stores:

- Candidate personal details
- Education details
- Skills
- Resume filename
- Unique candidate ID

This allows the API to **persist and retrieve candidate information reliably**.

---

## Notes

- Only **PDF, DOC, and DOCX** files are accepted.
- Resume files are stored in the `uploads/` directory.
- Candidate information is stored in **MongoDB database**.
- APIs can retrieve and filter stored candidates.

---

## Author

Adithya Hari

## Author

Adithya Hari
