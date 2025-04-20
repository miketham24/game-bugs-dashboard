import pandas as pd

# Load dataset
df = pd.read_csv("data/Sims4_Bug_Report_Dataset.csv")

# Convert date columns to datetime objects
df['date_reported'] = pd.to_datetime(df['date_reported'], errors='coerce')
df['date_resolved'] = pd.to_datetime(df['date_resolved'], errors='coerce')

# Check for nulls
print(df.isnull().sum())

# Add bug resolution time
df['days_to_resolve'] = (df['date_resolved'] - df['date_reported']).dt.days

# Standardize categorical fields
df['platform'] = df['platform'].str.title().str.strip()
df['severity'] = df['severity'].str.capitalize().str.strip()

# Remove bugs with negative resolution time (if any)
df = df[df['days_to_resolve'].isnull() | (df['days_to_resolve'] >= 0)]

# Preview
print(df.head())

df.to_csv("data/Sims4_Bug_Report_Dataset_Cleaned.csv", index=False)