#!/usr/bin/env bash
set -e

echo "=============================="
echo "E2E SYSTEM VALIDATION STARTED"
echo "=============================="

export PYTHONPATH=src

echo "[1/7] Bootstrapping database"
python scripts/bootstrap_db.py

echo "[2/7] Seeding organization"
python scripts/seed_org.py || true

echo "[3/7] Running unit tests"
pytest tests/unit

echo "[4/7] Starting API (background)"
uvicorn yt_trending.api.main:app --port 8001 &
API_PID=$!
sleep 3

echo "[5/7] Health check"
curl -s http://127.0.0.1:8001/health | grep ok

echo "[6/7] ML inference check"
curl -s -H "X-API-Key: demo-key" \
"http://127.0.0.1:8001/predict?region=IN&likes=50000&comments=8000&category_id=10&comments_disabled=false&ratings_disabled=false" \
| grep probability

echo "[7/7] Explainability check"
curl -s -H "X-API-Key: demo-key" \
"http://127.0.0.1:8001/explain?region=IN" \
| grep feature_importance

kill $API_PID

echo "=============================="
echo "E2E VALIDATION SUCCESSFUL"
echo "=============================="
