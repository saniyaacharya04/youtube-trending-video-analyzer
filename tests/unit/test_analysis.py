from yt_trending.services.analysis_service import basic_engagement_score
from yt_trending.domain.models import TrendingVideo
from datetime import datetime

def test_engagement_score():
    v = TrendingVideo("1", "t", 100, 10, 5, datetime.utcnow())
    assert basic_engagement_score(v) == 0.15
