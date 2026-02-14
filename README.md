# Mini Resume Collector Application

## Python Version
Python 3.10+

## Project Overview
This is a simple REST API built using FastAPI that allows candidates to submit resume details. The application validates input data and stores it in memory without using a database.

## Installation Steps

1. Clone the repository:
   git clone <repository-url>

2. Navigate into the project directory:
   cd miniresume-your-full-name

3. Create virtual environment:
   python -m venv venv

4. Activate virtual environment:
   Windows:
   venv\Scripts\activate

5. Install dependencies:
   pip install -r requirements.txt

## Run the Application

uvicorn main:app --reload

Application will run at:
http://127.0.0.1:8000

Swagger Documentation:
http://127.0.0.1:8000/docs

## API Endpoints

GET /  
Returns a welcome message.

GET /health  
Returns application health status.

POST /resumes  
Submit resume details.

GET /resumes  
Retrieve all submitted resumes.

## Example Request

POST /resumes

{
  "full_name": "John Doe",
  "email": "john@example.com",
  "phone": "9876543210",
  "skills": ["Python", "FastAPI"],
  "experience": 2
}

## Example Response

{
  "message": "Resume submitted successfully",
  "data": {
    "full_name": "John Doe",
    "email": "john@example.com",
    "phone": "9876543210",
    "skills": ["Python", "FastAPI"],
    "experience": 2
  }
}
