import pandas as pd
from sklearn.preprocessing import StandardScaler


file_path = 'winequality-red.csv'  
data = pd.read_csv(file_path)

print("Original Data:")
print(data.head())

X = data.iloc[:, :-1]  
y = data.iloc[:, -1]  

scaler = StandardScaler()
X_standardized = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

print("\nData after Standardization:")
print(X_standardized.head())

