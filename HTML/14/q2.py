a)
import numpy as np

flattened_array = np.array([1, 2, 3, 4, 5, 6])
weights = np.array([0.1, 0.2, 0.3, 0.2, 0.1, 0.1])
reshaped_array = flattened_array.reshape(2, 3)
reshaped_weights = weights.reshape(2, 3)

weighted_average = np.average(reshaped_array, axis=1, weights=reshaped_weights)

print("Flattened Array:")
print(flattened_array)

print("\nWeights:")
print(weights)

print("\nWeighted Average along axis=1:")
print(weighted_average)





b)
import pandas as pd

advertising_data = pd.read_csv('advertising.csv')
basic_stats = advertising_data.describe()

print("Basic Statistical Details of the Data:")
print(basic_stats)


