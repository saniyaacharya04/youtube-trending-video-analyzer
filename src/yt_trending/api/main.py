from fastapi import FastAPI, Depends
from yt_trending.api.auth import get_org
from yt_trending.api.usage import track_usage
from yt_trending.services.collection_service import fetch_trending_videos
from yt_trending.services.analysis_service import basic_engagement_score

app = FastAPI(title="YouTube Trending SaaS")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/trending")
def trending(org = Depends(get_org)):
    track_usage(org.id, "/trending")

    videos = fetch_trending_videos()
    return [
        {
            "video_id": v.video_id,
            "title": v.title,
            "engagement_score": basic_engagement_score(v)
        }
        for v in videos
    ]

@app.post("/billing/upgrade")
def billing_upgrade():
    return {"error": "Premium Feature – Placeholder"}, 402
