import pandas as pd

# Load the dataset
df = pd.read_csv("noshowappointments.csv")

print("Initial dataset shape:", df.shape)

# 1. Handle Missing Values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# (This dataset usually doesn't have many missing values, but it's good to check.)

# 2. Remove Duplicate Rows
df = df.drop_duplicates()
print("\nShape after dropping duplicates:", df.shape)

# 3. Standardize Text Values
# Standardizing the 'No-show' column
df['No-show'] = df['No-show'].str.strip().str.lower()
df['No-show'] = df['No-show'].replace({'yes': 1, 'no': 0})  # Convert to binary

# 4. Convert Date Columns to datetime
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])

# 5. Rename Columns for Consistency
df.columns = df.columns.str.strip().str.lower().str.replace('-', '_').str.replace(' ', '_')

# 6. Check and Fix Data Types
# Remove rows with negative ages
df = df[df['age'] >= 0]

# Ensure correct data types
df['age'] = df['age'].astype(int)
df['no_show'] = df['no_show'].astype(int)

# 7. Optional: Reset Index after cleaning
df.reset_index(drop=True, inplace=True)

# 8. Save the cleaned dataset
df.to_csv("cleaned_noshowappointments.csv", index=False)

print("\n✅ Cleaning complete. Cleaned dataset saved as 'cleaned_noshowappointments.csv'")
