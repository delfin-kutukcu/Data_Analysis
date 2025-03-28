import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def load_data():
    """Load the cleaned dataset."""
    project_root = Path(__file__).resolve().parent.parent
    datasets_path = project_root / "datasets"
    df = pd.read_csv(datasets_path / "music_videos_cleaned.csv")
    return df, project_root

def create_plots(df, save_path):
    """Generate and save visualizations."""
    save_path.mkdir(parents=True, exist_ok=True)
    
    # Histogram
    plt.figure(figsize=(8, 6))
    sns.histplot(df['Total Views'], kde=True)
    plt.title("Total Views Distribution")
    plt.savefig(save_path / "total_views_histogram.png")
    plt.close()

    # Boxplot
    plt.figure(figsize=(6, 5))
    sns.boxplot(y=df['Total Views'])
    plt.title("Views Boxplot")
    plt.savefig(save_path / "total_views_boxplot.png")
    plt.close()

    # Top 10 artists by total views
    top_artists = df.groupby('Artist')['Total Views'].sum().nlargest(10)
    plt.figure(figsize=(10, 6))
    top_artists.plot(kind='bar', color='skyblue')
    plt.title("Top 10 Artists by Total Views")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_path / "top_10_artists_bar.png")
    plt.close()

    # Combined 4-panel figure
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    sns.histplot(df['Total Views'], kde=True)
    plt.title("Total Views Distribution")

    plt.subplot(2, 2, 2)
    sns.boxplot(y=df['Total Views'])
    plt.title("Views Boxplot")

    plt.subplot(2, 2, 3)
    top_artists.plot(kind='bar', color='skyblue')
    plt.title("Top 10 Artists by Total Views")
    plt.xticks(rotation=45)

    plt.subplot(2, 2, 4)
    plt.text(0.5, 0.5, 'Not enough numeric columns\nfor correlation matrix',
             ha='center', va='center')
    plt.title("Correlation Matrix (Not Available)")

    plt.tight_layout()
    plt.savefig(save_path / "summary_4plots.png")
    plt.close()

if __name__ == "__main__":
    df, root = load_data()
    create_plots(df, root / "visuals")
    print("✅ Visualizations saved in /visuals/")
