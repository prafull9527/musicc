a)
import pandas as pd
import matplotlib.pyplot as plt

iris_data = pd.read_csv('iris.csv')
species_counts = iris_data['Species'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Iris Species Distribution')
plt.show()



b)
import pandas as pd

wine_data = pd.read_csv('winequality-red.csv')
basic_stats = wine_data.describe()

print("Basic Statistical Details of the Data:")
print(basic_stats)



