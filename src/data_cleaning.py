# data_cleaning.py
import pandas as pd

def clean_trending_data(file_path='data/raw/trending_videos.csv'):
    df = pd.read_csv(file_path)
    
    # Convert date
    df['published_date'] = pd.to_datetime(df['published_date'])
    
    # Replace missing values with 0
    df['likes'] = df['likes'].fillna(0)
    df['comments'] = df['comments'].fillna(0)
    
    # Add title length feature
    df['title_length'] = df['title'].apply(len)
    
    # Engagement ratio
    df['engagement_ratio'] = (df['likes'] + df['comments']) / df['views']
    
    df.to_csv('data/processed/trending_videos_clean.csv', index=False)
    return df

if __name__ == "__main__":
    df = clean_trending_data()
    print("Cleaned data saved to data/processed/trending_videos_clean.csv")
