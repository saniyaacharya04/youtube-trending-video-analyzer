from datetime import datetime
from yt_trending.domain.models import TrendingVideo

def fetch_trending_videos():
    # Simulated fetch (replace with YouTube API later)
    return [
        TrendingVideo(
            video_id="abc123",
            title="Sample Trending Video",
            views=120000,
            likes=5600,
            comments=430,
            fetched_at=datetime.utcnow()
        )
    ]
