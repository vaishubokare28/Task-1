import pandas as pd
import zipfile

# Full path to your zip file
zip_path = r'C:\Users\vaish\Downloads\archive.zip'

# Load CSV from ZIP
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    print("Files in ZIP:", zip_ref.namelist())  # Check contents
    with zip_ref.open('amazon.csv') as file:
        df = pd.read_csv(file)

print("Initial data:")
print(df.head())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 🚨 Replace 'column_name' with actual column names before using them!
# Example: Fill missing 'rating' and 'rating_count'
if 'rating' in df.columns:
    df['rating'].fillna('Unknown', inplace=True)
    df['rating'].fillna(method='ffill', inplace=True)

if 'rating_count' in df.columns:
    df['rating_count'].fillna(0, inplace=True)

# Drop rows with any remaining missing values
df.dropna(inplace=True)

# Remove duplicates
df = df.drop_duplicates()

# Standardize one text column (example: 'user_name') if it exists
if 'user_name' in df.columns:
    df['user_name'] = df['user_name'].str.strip().str.lower()

# Replace gender variants if 'gender' column exists
if 'gender' in df.columns:
    df['gender'] = df['gender'].replace({'Male': 'male', 'M': 'male', 'F': 'female', 'Female': 'female'})

# Standardize all text columns
text_cols = df.select_dtypes(include='object').columns
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.lower()

# Convert date column (if exists) to datetime
if 'date_column' in df.columns:
    df['date_column'] = pd.to_datetime(df['date_column'], format='%d-%m-%Y', errors='coerce')

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert price (remove ₹ and commas)
if 'price' in df.columns:
    df['price'] = pd.to_numeric(df['price'].str.replace('₹', '').str.replace(',', ''), errors='coerce')

# Convert types safely
if 'age' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors='coerce').fillna(0).astype(int)

if 'rating' in df.columns:
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Show final dtypes
print("\nFinal data types:")
print(df.dtypes)

# Export cleaned CSV
df.to_csv("cleaned_data.csv", index=False)
print("\n✅ Cleaned data saved as 'cleaned_data.csv'")
