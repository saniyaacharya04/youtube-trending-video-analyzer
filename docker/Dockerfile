FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt fastapi uvicorn sqlalchemy httpx

COPY src ./src
COPY scripts ./scripts

RUN python scripts/bootstrap_db.py

CMD ["uvicorn", "yt_trending.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
