import pandas as pd

# Sample dataset
data = {
    'Department': ['HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Salary': [50000, 60000, 75000, 52000, 61000, 78000, 54000],
    'Age': [25, 28, 30, 26, 29, 32, 27]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the dataset
print("Original Dataset:\n", df)

# Group by Department and calculate sum, mean, and max of Salary
grouped = df.groupby('Department')['Salary'].agg(['sum', 'mean', 'max'])

print("\nAggregated Salary Data by Department:\n", grouped)

# Group by Department and calculate multiple aggregates for multiple columns
multi_agg = df.groupby('Department').agg({
    'Salary': ['sum', 'mean', 'max'],
    'Age': ['mean', 'min', 'max']
})

print("\nAggregated Salary and Age Data by Department:\n", multi_agg)
