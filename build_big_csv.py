import os
import gzip
import pandas as pd

# Define the path to the data folder
data_folder = 'data'

# Initialize an empty list to store DataFrames
dataframes = []

# Loop through each .gz file in the data folder
for filename in os.listdir(data_folder):
    if filename.endswith('.gz'):
        file_path = os.path.join(data_folder, filename)
        
        # Open the .gz file and read the CSV inside
        with gzip.open(file_path, 'rt') as f:
            df = pd.read_csv(f)
            dataframes.append(df)

# Concatenate all DataFrames into one large DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('combined.csv', index=False)