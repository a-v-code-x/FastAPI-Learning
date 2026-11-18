
# FastAPI Learning & Projects

Welcome to my FastAPI learning repository! This repository contains my hands-on practice, backend development exercises, and projects built using **Python and FastAPI**.

The goal of this repository is to strengthen my understanding of backend development, REST APIs, request validation, exception handling, and database integration.

## Technologies Used

- Python
- FastAPI
- Pydantic
- SQLModel
- Uvicorn
- REST APIs

## Repository Structure

```text
FastAPI/
│
├── 02pincode/
│   ├── main.py
│   ├── models.py
│   ├── data.py
│   ├── exceptions.py
│   ├── requirements.txt
│   └── README.md
│
├── RANGMANCH-REVIEW/
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   └── README.md
│
└── README.md
```

## Projects

### 1. PIN Code Lookup API

A REST API developed using FastAPI that provides location information based on Indian PIN codes.

**Features:**
- Retrieve city, state, and district using a PIN code.
- Validate six-digit PIN code formats.
- Support bulk PIN code lookup.
- Handle invalid PIN codes using custom exceptions.
- Return structured JSON responses.

**Technologies:** Python, FastAPI, Pydantic

[Explore PIN Code API](./02pincode/)

### 2. RANGMANCH-REVIEW

A separate FastAPI project directory containing the initial application and model files.

The implementation is currently pending.

**Technologies:** Python, FastAPI, SQLModel

[Explore RANGMANCH-REVIEW](./RANGMANCH-REVIEW/)

## Key Concepts I'm Learning

- REST API Development
- HTTP Methods (GET, POST, PUT, DELETE)
- Path Parameters and Query Parameters
- Request and Response Models
- Pydantic Data Validation
- Exception Handling
- API Documentation with Swagger UI
- Backend Application Structure
- Database Integration

## Installation

Clone the repository:

```bash
git clone <YOUR_REPOSITORY_URL>
```

Navigate to a project folder:

```bash
cd FastAPI/02pincode
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --reload
```

## API Documentation

Once the application is running, access:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Learning Approach

This repository reflects my continuous learning journey in Python backend development.

I will keep adding new concepts, experiments, and projects as I improve my understanding of FastAPI and backend engineering.

## Author

**Arpit Vishwakarma**

- GitHub: [a-v-code-x](https://github.com/a-v-code-x)
- HackerRank: [Profile](https://www.hackerrank.com/profile/Arpitvishwakarm4)
- LeetCode: [Profile](https://leetcode.com/u/Ar_vish/)
