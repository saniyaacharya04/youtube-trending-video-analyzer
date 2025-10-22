# main.py
import streamlit as st
import pandas as pd
from setup_paths import setup_project_paths
from src.analysis import load_data, top_videos_by_views, top_videos_by_engagement
from src.visualization import plot_top_views, plot_engagement_ratio

# --- Setup project paths ---
paths = setup_project_paths()
RAW_DIR = paths["RAW_DIR"]
PROCESSED_DIR = paths["PROCESSED_DIR"]

# --- Define CSV file path dynamically ---
df_path = RAW_DIR / "trending_videos.csv"

st.title("YouTube Trending Video Analyzer")

# --- Load Data ---
try:
    df = load_data(df_path)  # Pass dynamic path
    st.success(f"Loaded data from {df_path}")
except FileNotFoundError:
    st.error(f"Data file not found at {df_path}. Please fetch data first.")
    st.stop()

# --- Top 10 Videos by Views ---
st.header("Top 10 Videos by Views")
top_views = top_videos_by_views(df)
st.table(top_views[['title', 'channel', 'views']])

# --- Top 10 Videos by Engagement Ratio ---
st.header("Top 10 Videos by Engagement Ratio")
top_engagement = top_videos_by_engagement(df)
st.table(top_engagement[['title', 'channel', 'engagement_ratio']])

# --- Visualizations ---
st.header("Visualizations")

st.subheader("Top Views")
plot_top_views(df)

st.subheader("Top Engagement Ratio")
plot_engagement_ratio(df)
