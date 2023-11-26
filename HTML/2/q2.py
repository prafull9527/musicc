a)
import pandas as pd

# Load the data from the CSV file
data = pd.read_csv('Data.csv')
print("Original Data:")
print(data)
data['salary'].fillna(data['salary'].mean(), inplace=True)
data['age'].fillna(data['age'].mean(), inplace=True)
print("\nData after handling missing values:")
print(data)
data.to_csv('Modified_Data.csv', index=False)

print("\nModified data saved to 'Modified_Data.csv'")


b)
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
data.sort_values(by='name', inplace=True)
plt.figure(figsize=(10, 6))
plt.plot(data['name'], data['salary'], marker='o', linestyle='-', color='b')
plt.title('Line Plot of Name vs Salary')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.xticks(rotation=45, ha='right') 
plt.tight_layout()

plt.show()



c)
import pandas as pd
import numpy as np

file_path = 'heights_weights.csv' 
data = pd.read_csv(file_path)

print("First 10 rows:")
print(data.head(10))

print("\nLast 10 rows:")
print(data.tail(10))

print("\nRandom 20 rows:")
print(data.sample(20))

print("\nDataset shape:")
print(data.shape)



