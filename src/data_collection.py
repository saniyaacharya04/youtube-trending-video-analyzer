# data_collection.py
from googleapiclient.discovery import build
import pandas as pd
from src.config import YOUTUBE_API_KEY

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def fetch_trending_videos(region='US', max_results=50):
    request = youtube.videos().list(
        part='snippet,statistics',
        chart='mostPopular',
        regionCode=region,
        maxResults=max_results
    )
    response = request.execute()
    videos = []
    for item in response['items']:
        videos.append({
            'video_id': item['id'],
            'title': item['snippet']['title'],
            'channel': item['snippet']['channelTitle'],
            'views': int(item['statistics'].get('viewCount', 0)),
            'likes': int(item['statistics'].get('likeCount', 0)),
            'comments': int(item['statistics'].get('commentCount', 0)),
            'published_date': item['snippet']['publishedAt'],
            'category_id': item['snippet'].get('categoryId', None)
        })
    df = pd.DataFrame(videos)
    df.to_csv('data/raw/trending_videos.csv', index=False)
    return df

if __name__ == "__main__":
    df = fetch_trending_videos()
    print("Trending videos saved to data/raw/trending_videos.csv")
