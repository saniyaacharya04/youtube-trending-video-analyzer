# analysis.py
import pandas as pd

def load_data(file_path='data/processed/trending_videos_clean.csv'):
    return pd.read_csv(file_path)

def top_videos_by_views(df, top_n=10):
    return df.sort_values('views', ascending=False).head(top_n)

def top_videos_by_engagement(df, top_n=10):
    return df.sort_values('engagement_ratio', ascending=False).head(top_n)
