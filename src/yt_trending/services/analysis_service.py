def basic_engagement_score(video):
    if video.views == 0:
        return 0
    return round((video.likes + video.comments) / video.views, 4)
