import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def clean_data(input_path, output_path):
    \"\"\"Clean and normalize dataset\"\"\"
    df = pd.read_csv(input_path)
    
    # Data cleaning steps
    df['Total Views'] = df['Total Views'].str.replace(',', '').astype(int)
    
    # Normalization
    scaler = MinMaxScaler()
    df['Views_Normalized'] = scaler.fit_transform(df[['Total Views']])
    
    df.to_csv(output_path, index=False)
    print(f\"Cleaned data saved to {output_path}\")

if __name__ == \"__main__\":
    clean_data('datasets/raw_data.csv', 'datasets/cleaned_data.csv')
