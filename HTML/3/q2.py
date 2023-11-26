a)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris_data = pd.read_csv('iris.csv')
sns.set(style="whitegrid")

plt.figure(figsize=(15, 10))
plt.subplot(2, 2, 1)
sns.boxplot(x='Species', y='SepalLengthCm', data=iris_data)
plt.title('Sepal Length Distribution')

plt.subplot(2, 2, 2)
sns.boxplot(x='Species', y='SepalWidthCm', data=iris_data)
plt.title('Sepal Width Distribution')

plt.subplot(2, 2, 3)
sns.boxplot(x='Species', y='PetalLengthCm', data=iris_data)
plt.title('Petal Length Distribution')

plt.subplot(2, 2, 4)
sns.boxplot(x='Species', y='PetalWidthCm', data=iris_data)
plt.title('Petal Width Distribution')
plt.tight_layout()

plt.show()



b)
import pandas as pd

file_path = 'heights_weights.csv'  
data = pd.read_csv(file_path)
basic_stats = data.describe()

print("Basic Statistical Details of the Data:")
print(basic_stats)




