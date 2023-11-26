import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

file_path = 'Data.csv' 
data = pd.read_csv(file_path)

print("Original Data:")
print(data)

onehot_encoder = OneHotEncoder(sparse=False, drop='first')
onehot_encoded = pd.DataFrame(onehot_encoder.fit_transform(data[['Country']]), columns=onehot_encoder.get_feature_names_out(['Country']))
data = pd.concat([data, onehot_encoded], axis=1)

data.drop('Country', axis=1, inplace=True)

print("\nData after OneHot encoding on 'Country' column:")
print(data)

label_encoder = LabelEncoder()
data['Purchased'] = label_encoder.fit_transform(data['Purchased'])

print("\nData after Label encoding on 'Purchased' column:")
print(data)

