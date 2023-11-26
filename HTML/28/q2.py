import pandas as pd
import numpy as np

data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank','Grace', 'Hank', 'Ivy', 'Jack'],'age': [25, 30, 22, 35, 28, 33, 26, 40, 24, 29],'percentage': [75.5, 88.2, 93.0, 65.8, 72.3, 81.7, 90.5, 78.0, 85.2,77.9]}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nDataFrame Information:")
print("Shape:", df.shape)
print("Number of Rows and Columns:", df.shape[0], "rows,", df.shape[1], "columns")
print("\nData Types:")
print(df.dtypes)
print("\nFeature Names:")
print(df.columns)
print("\nDescription of Data:")
print(df.describe())


print("\nBasic Statistical Details:")
print(df.describe())

additional_data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],'age': [25, 30, 22, np.nan, 28],'percentage': [75.5, 88.2, 93.0, 65.8, np.nan],'remarks': ['', '', '', '', '']}

df = df.append(pd.DataFrame(additional_data), ignore_index=True)

print("\nDataFrame with Duplicate and Missing Values:")
print(df)

