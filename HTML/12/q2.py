a)

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)  
random_array = np.random.randint(0, 100, 50)

# Line Chart
plt.figure(figsize=(12, 4))
plt.subplot(1, 4, 1)
plt.plot(random_array, marker='o', color='green', linestyle='-')
plt.title('Line Chart')
plt.xlabel('Index')
plt.ylabel('Value')

# Scatter Plot
plt.subplot(1, 4, 2)
plt.scatter(np.arange(50), random_array, color='blue', marker='o')
plt.title('Scatter Plot')
plt.xlabel('Index')
plt.ylabel('Value')

# Histogram
plt.subplot(1, 4, 3)
plt.hist(random_array, bins=15, color='orange', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Box Plot
plt.subplot(1, 4, 4)
plt.boxplot(random_array, vert=False, widths=0.7, patch_artist=True, boxprops=dict(facecolor='lightpink'))
plt.title('Box Plot')

plt.tight_layout()
plt.show()



b)

import pandas as pd
import numpy as np

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Alice', 'Bob', 'Charlie', 'David'],
    'salary': [50000, 60000, np.nan, 55000, 70000, np.nan, 50000, 60000, 55000, 60000],
    'department': ['HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

new_data = {
    'name': ['Alice', 'Eva', 'George', 'Frank', 'Alice', 'Bob', 'Alice', 'Charlie', 'David', 'Eva'],
    'salary': [51000, 72000, np.nan, 58000, 51000, 62000, 51000, 56000, 58000, np.nan],
    'department': ['HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR']
}

df = df.append(pd.DataFrame(new_data), ignore_index=True)

print("\nDataFrame after adding new rows:")
print(df)

df.dropna(inplace=True)
print("\nDataFrame after dropping null and empty values:")
print(df)

