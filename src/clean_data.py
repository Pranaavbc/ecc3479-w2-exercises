import pandas as pd 

# Read Raw CSV file 
input_path = "data/raw/sample_data.csv"
data = pd.read_csv(input_path)

# Rename unclear variables 
data = data.rename(columns={
    "unemployment_rate": "unemployment_rate_percent",
    "participation_rate": "labour_force_participation_percent"
})

# Handle data quality issues (missing values, duplicates, outliers)
data = data.drop_duplicates()  # Remove duplicates
data = data.dropna()  # Remove rows with missing values

data["state"] = data["state"].str.upper()

# Ensure numeric variables are numeric
data["unemployment_rate_percent"] = pd.to_numeric(data["unemployment_rate_percent"], errors="coerce")
data["labour_force_participation_percent"] = pd.to_numeric(data["labour_force_participation_percent"], errors="coerce")

# Remove rows that became NaN after conversion
data = data.dropna()

#save cleaned data to new CSV file
output_path = "data/clean/labour_data_clean.csv"
data.to_csv(output_path, index=False)

print("Cleaned dataset saved to:", output_path)