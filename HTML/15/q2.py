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
import matplotlib.pyplot as plt

subject_names = ['Math', 'English', 'Science', 'History', 'Art']
marks_obtained = [90, 85, 92, 88, 75]

plt.figure(figsize=(8, 8))
plt.pie(marks_obtained, labels=subject_names, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightskyblue', 'lightgreen', 'lightpink', 'lightyellow'])
plt.title('Marks Distribution in Subjects')
plt.show()




