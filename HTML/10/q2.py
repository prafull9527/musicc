a)
import pandas as pd

file_path = 'SOCR-HeightWeight.csv'
data = pd.read_csv(file_path)

mean_values = data.mean()
print("Column-wise Mean:")
print(mean_values)

median_values = data.median()
print("\nColumn-wise Median:")
print(median_values)

b)
def manhattan_distance(point1, point2):
return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def sum_of_manhattan_distances(points):
total_distance = 0
num_points = len(points)
for i in range(num_points - 1):
for j in range(i + 1, num_points):
total_distance += manhattan_distance(points[i], points[j])
return total_distance

points = [(1, 2), (3, 5), (7, 1), (4, 8)]
result = sum_of_manhattan_distances(points)
print("Sum of Manhattan distances:", result)

