import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from pathlib import Path

def clean_data(input_filename, output_filename, merge_filename=None):
    """Clean and normalize dataset from datasets folder and save back there."""
    project_root = Path(__file__).resolve().parent.parent
    datasets_path = project_root / "datasets"

    df = pd.read_csv(datasets_path / input_filename)

    # Data cleaning
    df['Total Views'] = df['Total Views'].str.replace(',', '').astype(int)

    # Optional merge
    if merge_filename:
        artist_path = datasets_path / merge_filename
        if artist_path.exists():
            artists_info = pd.read_csv(artist_path)
            df = df.merge(artists_info, on="Artist", how="left")
            print("Merged with artist info.")

    # Normalization
    scaler = MinMaxScaler()
    df['Views_Normalized'] = scaler.fit_transform(df[['Total Views']])

    df.to_csv(datasets_path / output_filename, index=False)
    print(f"Cleaned data saved to {datasets_path / output_filename}")

if __name__ == "__main__":
    clean_data("music_videos.csv", "music_videos_cleaned.csv", merge_filename="artists_info.csv")
