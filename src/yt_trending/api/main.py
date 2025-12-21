from fastapi import FastAPI
from yt_trending.services.collection_service import fetch_trending_videos
from yt_trending.services.analysis_service import basic_engagement_score

app = FastAPI(title="YouTube Trending Video Analyzer")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/trending")
def trending():
    videos = fetch_trending_videos()
    return [
        {
            "video_id": v.video_id,
            "title": v.title,
            "views": v.views,
            "likes": v.likes,
            "comments": v.comments,
            "engagement_score": basic_engagement_score(v)
        }
        for v in videos
    ]
