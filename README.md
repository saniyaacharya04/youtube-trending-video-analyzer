# YouTube Trending Video Analyzer

An end-to-end, production-grade backend system that analyzes YouTube trending data and provides **real-time popularity prediction**, **explainable ML inference**, and **region-aware analytics** through a FastAPI service.

This project demonstrates **full ownership** across data ingestion, ML training, API design, SaaS-style authentication, CI/CD, Dockerization, and end-to-end validation.

---

## Key Capabilities

* Real YouTube trending data ingestion from Kaggle
* Machine learning model trained on historical engagement signals
* Region-aware inference (IN / US)
* Explainable predictions using feature importance
* FastAPI backend with API-key based access control
* SQLite persistence for usage tracking
* Dockerized deployment
* CI pipeline with unit + E2E tests
* One-command local setup using Makefile

---

## System Architecture

```
Kaggle CSV Data
      ↓
Data Processing & Feature Engineering
      ↓
Region-specific ML Training (RandomForest)
      ↓
Saved Models (per region)
      ↓
FastAPI Service
      ├── /predict   → Live ML inference
      ├── /explain   → Feature importance
      └── /health    → System check
```

---

## Tech Stack

**Backend**

* Python 3.10
* FastAPI
* SQLAlchemy
* SQLite

**Machine Learning**

* scikit-learn
* pandas, numpy
* joblib

**DevOps**

* Docker & Docker Compose
* GitHub Actions (CI)
* Makefile automation

**Testing**

* pytest (unit + E2E)
* HTTPX

---

## Repository Structure

```
.
├── data/                  # Raw & processed datasets (ignored in git)
├── docker/                # Dockerfile and compose setup
├── models/                # Trained ML models (generated locally)
├── notebooks/             # Data exploration & analysis
├── scripts/               # Bootstrap, dataset download, E2E validation
├── src/yt_trending/       # Application source code
│   ├── api/               # FastAPI routes & auth
│   ├── core/              # Config & DB session
│   ├── domain/            # ORM models
│   ├── ml/                # Model training
│   └── services/          # Business logic
├── tests/                 # Unit and E2E tests
├── Makefile
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Environment Setup

```bash
conda create -n yt-trending python=3.10
conda activate yt-trending
make install
```

---

### 2. Download Dataset (Kaggle)

Ensure `~/.kaggle/kaggle.json` is configured.

```bash
make download-data
```

This downloads the official **YouTube Trending Video Statistics** dataset and prepares region-specific CSVs.

---

### 3. Train Models

```bash
make train
```

Trains separate models for:

* India (IN)
* United States (US)

Models are generated locally in `models/`.

---

### 4. Run the API

```bash
make run
```

API runs at:

```
http://127.0.0.1:8000
```

---

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{ "status": "ok" }
```

---

### Predict Popularity

```http
GET /predict
```

Query Parameters:

* `region` (IN | US)
* `likes`
* `comments`
* `category_id`
* `comments_disabled`
* `ratings_disabled`

Header:

```
X-API-Key: demo-key
```

Example:

```bash
curl -H "X-API-Key: demo-key" \
"http://127.0.0.1:8000/predict?region=IN&likes=50000&comments=8000&category_id=10&comments_disabled=false&ratings_disabled=false"
```

Response:

```json
{
  "region": "IN",
  "popularity_probability": 0.76
}
```

---

### Explain Prediction

```http
GET /explain?region=IN
```

Response:

```json
{
  "region": "IN",
  "feature_importance": {
    "likes": 0.5383,
    "comment_count": 0.3316,
    "category_id": 0.1246,
    "comments_disabled": 0.0038,
    "ratings_disabled": 0.0017
  }
}
```

---

## Testing & Validation

### Unit Tests

```bash
make test
```

---

### Full End-to-End Validation

```bash
make e2e
```

This validates:

* Database bootstrap
* Org seeding (idempotent)
* API startup
* Health endpoint
* ML inference
* Explainability output

---

## CI Pipeline

GitHub Actions automatically runs on every push and pull request:

* Dependency installation
* Database bootstrap
* Unit tests
* End-to-end validation

CI definition:

```
.github/workflows/ci.yml
```

---

## What This Project Demonstrates

* Backend system design
* Real ML inference in production APIs
* Explainable ML outputs
* Data-driven feature engineering
* SaaS-style API authentication
* Clean repository hygiene
* CI/CD readiness
* Dockerized deployment

---

## License

MIT License

