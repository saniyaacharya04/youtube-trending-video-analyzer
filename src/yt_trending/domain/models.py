from dataclasses import dataclass
from datetime import datetime

@dataclass
class TrendingVideo:
    video_id: str
    title: str
    views: int
    likes: int
    comments: int
    fetched_at: datetime
