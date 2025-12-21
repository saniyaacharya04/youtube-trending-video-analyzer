FROM python:3.10-slim

WORKDIR /app

# Install deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt fastapi uvicorn sqlalchemy httpx

# Copy source
COPY src ./src
COPY scripts ./scripts

# Add src to PYTHONPATH
ENV PYTHONPATH=/app/src

# Init DB
RUN python scripts/bootstrap_db.py

EXPOSE 8000

CMD ["uvicorn", "yt_trending.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
