# Importing Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the CSV file and preprocessing the DataFrame
df=pd.read_csv('/content/cars_24_combined.csv').drop(['Unnamed: 0'], axis=1).drop_duplicates()
df.head()

# Displaying information about the DataFrame
df.info()

# Handling missing values in specific columns
df["Location"].fillna("None", inplace=True)
#df["Year"].fillna("None", inplace=True)
df["Car Name"].fillna("None", inplace=True)

# Checking for remaining missing values in the DataFrame
df.isnull().sum()

# Converting 'Year' and 'Price' columns to appropriate data types and dropping rows with missing 'Year'
df['Year'] = df['Year'].astype(int)
df['Year'] = df['Year'].fillna(0).astype(int)
df = df.dropna(subset=['Year'])
df['Year'] = df['Year'].astype(int)
df['Price']=df['Price'].astype(int)
df.head()

# Data cleaning and transformation for 'Location' column
df['Location'] = df['Location'].replace('[\d-]', '', regex=True)

df['Location'].unique()

# Mapping abbreviations to full state names in 'Location' column
mapping_dict = { 'HR': 'Haryana',
    'TN': 'Tamil Nadu',
    'TS': 'Telangana',
    'WB': 'West Bengal',
    'MH': 'Maharashtra',
    'None': None,
    'UP': 'Uttar Pradesh',
    'KA': 'Karnataka',
    'PB': 'Punjab',
    'GJ': 'Gujarat',
    'DLC': 'Delhi',
    'DL': 'Delhi',
    'CH': 'Chandigarh',
    'KL': 'Kerala',
    'RJ': 'Rajasthan',
    'BR': 'Bihar',
    'AP': 'Andhra Pradesh',
    'MP': 'Madhya Pradesh',
    'BH': 'Bihar'}

df['Location'] = df['Location'].replace(mapping_dict)

df.head()

# Displaying information about the cleaned DataFrame
df.info()

# Data visualization - Fuel vs. Price Bar Plot
fuel = df['Fuel']
price = df['Price']
sns.barplot(x=fuel,y=price)
plt.xlabel('Fuel')
plt.ylabel('Price')
plt.title('Fuel vs. Price Scatter Plot')

# Displaying the top 5 car types based on average price
df.groupby(['Car Name','Type']).agg({'Price':'mean'}).sort_values("Price",ascending=False).reset_index()[:5]

# Data visualization - Owner vs. Price Bar Plot
Owner = df['Owner']
price = df['Price']
sns.barplot(x=Owner, y=price)
plt.xlabel('Owner')
plt.ylabel('Price')
plt.title('Owner vs. Price Scatter Plot')

# Data visualization - Distance vs. Price Scatter Plot
distance = df['Distance']
price = df['Price']
plt.scatter(distance, price)
plt.xlabel('Distance')
plt.ylabel('Price')
plt.title('Distance vs. Price Scatter Plot')

# Data visualization - Driving Type vs. Price Bar Plot
sns.barplot(x='Drive', y='Price', data=df)

# Set labels and title
plt.xlabel('Driving Type')
plt.ylabel('Price')
plt.title('Driving Type vs. Price')

# Displaying information about the DataFrame
df.info()

# Encoding categorical columns using LabelEncoder
from sklearn.preprocessing import LabelEncoder
categorical_columns = ['Car Name', 'Fuel', 'Drive','Type','Location']
label_encoder = LabelEncoder()
for i in categorical_columns:
  df[i]=label_encoder.fit_transform(df[i])

# Displaying the encoded DataFrame
print(df)

# Calculating and visualizing the correlation heatmap
correlation_matrix = df.corr()
plt.figure(figsize=(20, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Splitting the data into training and testing sets for machine learning model
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

X=df.drop('Price',axis=1)
y=df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Creating and training a RandomForestRegressor model
rf_model= RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train,y_train)


knn_classifier = KNeighborsClassifier(n_neighbors=3)
knn_classifier.fit(X_train, y_train)
y_pred = knn_classifier.predict(X_test)

# Evaluating the RandomForestRegressor model
y_pred=rf_model.predict(X_test)
mse=mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Displaying the predicted prices and the original prices in a DataFrame
print(y_pred)
results_df = pd.DataFrame({'Original': y_test, 'Predicted': y_pred})
print(results_df)
