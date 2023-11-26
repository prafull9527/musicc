a)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris_data = pd.read_csv('iris.csv')

plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
sns.boxplot(x='Species', y='SepalLengthCm', data=iris_data)
plt.title('Sepal Length distribution across Species')

plt.subplot(2, 2, 2)
sns.boxplot(x='Species', y='SepalWidthCm', data=iris_data)
plt.title('Sepal Width distribution across Species')

plt.subplot(2, 2, 3)
sns.boxplot(x='Species', y='PetalLengthCm', data=iris_data)
plt.title('Petal Length distribution across Species')

plt.subplot(2, 2, 4)
sns.boxplot(x='Species', y='PetalWidthCm', data=iris_data)
plt.title('Petal Width distribution across Species')

plt.tight_layout()
plt.show()







b)
import pandas as pd

file_path = 'your_dataset.csv'
data = pd.read_csv(file_path)

print("First 5 Rows:")
print(data.head())

print("\nLast 5 Rows:")
print(data.tail())

print("\nRandom 10 Rows:")
print(data.sample(10))

