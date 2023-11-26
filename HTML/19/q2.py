import pandas as pd
import numpy as np
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],'age': [25, 30, 22, 28, 24, 35, 27, 32, 23, 29],'percentage': [85.5, 92.3, 78.9, 88.2, 95.1, 87.6, 90.0, 78.3, 93.5, 86.7]}

df = pd.DataFrame(data)

print("Task 1: Dataframe with 10 rows")
print(df)

print("\nTask 2: Dataframe Information")
print("Shape of the Data:", df.shape)
print("Number of Rows:", len(df))
print("Number of Columns:", len(df.columns))
print("\nData Types and Feature Names:")
print(df.dtypes)
print("\nDescription of the Data:")
print(df.describe())

additional_data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age': [25, 30, np.nan, 28, 24],
    'percentage': [85.5, 92.3, 78.9, np.nan, 95.1],
    'remarks': [np.nan] * 5
}

df = df.append(pd.DataFrame(additional_data), ignore_index=True)
print("\nTask 3: Dataframe after adding 5 rows with duplicate and missing values")
print(df)

