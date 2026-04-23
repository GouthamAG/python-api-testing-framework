# Python API Testing Framework

## Overview
This project is a basic API automation framework built using Python, pytest, and requests.

It demonstrates how to design a scalable test structure with reusable components and clean architecture.

---

## Tech Stack
- Python
- pytest
- requests
- pytest-html

---

## Features
- API client using requests.Session
- Centralized header management (API key support)
- Basic API test coverage (GET)
- HTML test reporting

---

## Project Structure

tests/         # Test cases  
utils/         # API client and reusable utilities  
config/        # Configuration (base URL, API key)  
conftest.py    # pytest fixtures  
requirements.txt  
README.md  

---

## Setup Instructions

### 1. Clone the repository
git clone <your-repo-url>  
cd python-api-testing-framework  

### 2. Create virtual environment
python -m venv venv  

Mac/Linux:
source venv/bin/activate  

Windows:
venv\Scripts\activate  

### 3. Install dependencies
pip install -r requirements.txt  

---

## Running Tests

pytest --html=report.html  

After execution, open `report.html` in your browser to view results.

---

## Sample Test Covered
- GET users API validation  
- Status code verification  
- Response structure validation  

---

## Future Improvements
- Add POST / PUT / DELETE API tests  
- Authentication token handling  
- Logging (request & response)  
- Schema validation  
- CI integration using GitHub Actions  

---

## Author
Goutham A G