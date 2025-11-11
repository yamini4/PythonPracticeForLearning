import pandas as pd
import numpy as np

# Create a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [25, np.nan, 30, 22, 28],
    'City': ['Delhi', 'Mumbai', None, 'Chennai', 'Kolkata']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the dataset
print("Dataset:\n", df)

# Check for missing values (NaN or None)
print("\nMissing values in each column:\n", df.isnull().sum())

# Optionally, check if any row has missing values
print("\nRows with missing values:\n", df[df.isnull().any(axis=1)])
