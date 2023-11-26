import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Binarizer

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(url, sep=';')

X = data.drop('quality', axis=1)
y = data['quality']

scaler_minmax = MinMaxScaler()
X_minmax = scaler_minmax.fit_transform(X)

scaler_standard = StandardScaler()
X_standard = scaler_standard.fit_transform(X)

binarizer = Binarizer(threshold=3.5) 
X_binarized = binarizer.fit_transform(X)

print("Original Data:")
print(X.head())

print("\nRescaled Data:")
print(pd.DataFrame(X_minmax, columns=X.columns).head())

print("\nStandardized Data:")
print(pd.DataFrame(X_standard, columns=X.columns).head())

print("\nBinarized Data:")
print(pd.DataFrame(X_binarized, columns=X.columns).head())

