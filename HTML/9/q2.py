a)
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)  
random_array = np.random.randint(0, 100, 50)

# Line Chart
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(random_array, marker='o', color='green', linestyle='-', linewidth=2, markersize=8)
plt.title('Line Chart')
plt.xlabel('Index')
plt.ylabel('Value')

# Scatter Plot
plt.subplot(1, 2, 2)
plt.scatter(np.arange(50), random_array, color='blue', marker='o', s=80,alpha=0.7)
plt.title('Scatter Plot')
plt.xlabel('Index')
plt.ylabel('Value')

plt.tight_layout()
plt.show()



b)
import matplotlib.pyplot as plt

subject_names = ['Math', 'English', 'Science', 'History', 'Art']
marks_obtained = [90, 85, 92, 88, 75]

plt.figure(figsize=(8, 8))
plt.pie(marks_obtained, labels=subject_names, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightskyblue', 'lightgreen','lightpink', 'lightyellow'])
plt.title('Marks Distribution in Subjects')
plt.show()




c)
import pandas as pd

file_path = 'winequality-red.csv' 
data = pd.read_csv(file_path)

print("a) Describing the Dataset:")
print(data.describe())

print("\nb) Shape of the Dataset:")
print(data.shape)

print("\nc) Displaying first 3 rows from the Dataset:")
print(data.head(3))





