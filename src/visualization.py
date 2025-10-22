# visualization.py
import seaborn as sns
import matplotlib.pyplot as plt

def plot_top_views(df, top_n=10):
    top = df.sort_values('views', ascending=False).head(top_n)
    sns.barplot(x='views', y='title', data=top)
    plt.title('Top Videos by Views')
    plt.show()

def plot_engagement_ratio(df, top_n=10):
    top = df.sort_values('engagement_ratio', ascending=False).head(top_n)
    sns.barplot(x='engagement_ratio', y='title', data=top)
    plt.title('Top Videos by Engagement Ratio')
    plt.show()
