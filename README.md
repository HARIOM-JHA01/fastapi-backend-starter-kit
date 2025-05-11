# FastAPI Project

A production-ready FastAPI project template.

## Features
- FastAPI for building APIs
- Modular app structure (api, core, crud, database, models, schemas)
- Environment variable support via `.env` (see `.env.sample`)
- Docker support
- Requirements managed in `requirements.txt`

## Project Structure
```
app/
  main.py            # FastAPI entrypoint
  api/               # API routes
  core/              # Core settings, config, security
  crud/              # CRUD operations
  database/          # Database session and init
  models/            # SQLAlchemy models
  schemas/           # Pydantic schemas
```

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/HARIOM-JHA01/fastapi-backend-starter-kit.git
cd fastapi-backend-starter-kit
```

### 2. Create and configure your environment
- Copy `.env.sample` to `.env` and update values as needed.

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
uvicorn app.main:app --reload
```

### 5. API Docs
Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive API documentation.

### 6. Using Docker
Build and run the app with Docker:
```bash
docker build -t fastapi-backend-starter-kit .
docker run -d -p 8000:8000 fastapi-backend-starter-kit
```

## License
MIT
