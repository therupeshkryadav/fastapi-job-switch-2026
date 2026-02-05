# Backend Learning Track

A comprehensive learning path for backend development using FastAPI and PostgreSQL.

## Phases

### Phase 0: Python basics
- Location: `phase-0-python-basics/`
- Simple interactive scripts to learn Python input/output and basic types
- Includes `myapp.py` demonstrating input, basic math, and string formatting

### Phase 1: FastAPI Basics
- Location: `phase-1-fastapi-basics/`
- In-memory student management API
- Demonstrates core FastAPI concepts
- No database persistence

### Phase 2: PostgreSQL Backend
- Location: `phase-2-postgresql-backend/`
- Full-stack FastAPI application with PostgreSQL
- SQLAlchemy ORM integration
- Docker containerization
- Production-ready architecture

## Getting Started

Each phase has its own README with detailed setup instructions.

## Prerequisites

- Python 3.11+
- Docker & Docker Compose (for Phase 2)
- PostgreSQL (optional, for manual setup)

## Repository Structure

```
backend-learning-track/
├── README.md
├── phase-0-python-basics/
│   ├── myapp.py
│   └── README.md
├── phase-1-fastapi-basics/
│   ├── myapi.py
│   └── README.md
└── phase-2-postgresql-backend/
    ├── app/
    │   ├── main.py
    │   ├── api/
    │   ├── schemas/
    │   ├── models/
    │   ├── crud/
    │   ├── services/
    │   ├── db/
    │   └── tests/
    ├── Dockerfile
    ├── docker-compose.yml
    └── README.md
```