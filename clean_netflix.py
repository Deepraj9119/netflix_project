import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Step 2: View the first few rows
print("🔹 First 5 rows of the dataset:")
print(df.head())

# Step 3: Check for missing values
print("\n🔹 Missing values per column:")
print(df.isnull().sum())

# Step 4: Remove duplicate rows
df = df.drop_duplicates()

# Step 5: Rename column headers (lowercase + underscores)
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Step 6: Fill missing values (use new column names)
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['date_added'] = df['date_added'].fillna('01-Jan-2000')

# Step 7: Standardize text columns
df['type'] = df['type'].str.lower().str.strip()
df['country'] = df['country'].str.lower().str.strip()
df['listed_in'] = df['listed_in'].str.lower().str.strip()

# Step 8: Convert 'date_added' to datetime format
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Step 9: Check and fix data types
if 'release_year' in df.columns:
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce').fillna(0).astype(int)

# Step 10: Save cleaned data
df.to_csv("cleaned_netflix_titles.csv", index=False)

# Step 11: Summary of cleaning
print("\n✅ Data Cleaning Summary:")
print("- Filled missing values in 'director', 'cast', 'country', and 'date_added'")
print("- Removed duplicate rows")
print("- Standardized text values in 'type', 'country', and 'listed_in'")
print("- Converted 'date_added' to datetime format")
print("- Renamed column headers to lowercase with underscores")
print("- Ensured 'release_year' is in integer format")
print("\n🎉 Cleaned data saved as 'cleaned_netflix_titles.csv'")