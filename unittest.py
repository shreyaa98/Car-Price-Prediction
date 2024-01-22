import unittest
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

class TestCarAnalysis(unittest.TestCase):

    def setUp(self):
        # Load the dataset and preprocess it
        self.df = pd.read_csv('/content/cars_24_combined.csv').drop(['Unnamed: 0'], axis=1).drop_duplicates()
        self.df["Location"].fillna("None", inplace=True)
        self.df["Car Name"].fillna("None", inplace=True)
        self.df['Year'] = self.df['Year'].fillna(0).astype(int)
        self.df = self.df.dropna(subset=['Year'])
        self.df['Year'] = self.df['Year'].astype(int)
        self.df['Price'] = self.df['Price'].astype(int)
        self.df['Location'] = self.df['Location'].replace('[\d-]', '', regex=True)
        mapping_dict = {'HR': 'Haryana', 'TN': 'Tamil Nadu', 'TS': 'Telangana', 'WB': 'West Bengal',
                        'MH': 'Maharashtra', 'None': None, 'UP': 'Uttar Pradesh', 'KA': 'Karnataka',
                        'PB': 'Punjab', 'GJ': 'Gujarat', 'DLC': 'Delhi', 'DL': 'Delhi', 'CH': 'Chandigarh',
                        'KL': 'Kerala', 'RJ': 'Rajasthan', 'BR': 'Bihar', 'AP': 'Andhra Pradesh',
                        'MP': 'Madhya Pradesh', 'BH': 'Bihar'}
        self.df['Location'] = self.df['Location'].replace(mapping_dict)
        categorical_columns = ['Car Name', 'Fuel', 'Drive', 'Type', 'Location']
        label_encoder = LabelEncoder()
        for col in categorical_columns:
            self.df[col] = label_encoder.fit_transform(self.df[col])

        # Split the data for testing the machine learning model
        X = self.df.drop('Price', axis=1)
        y = self.df['Price']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the Random Forest model
        self.rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.rf_model.fit(self.X_train, self.y_train)

        # Train the KNN classifier
        self.knn_classifier = KNeighborsClassifier(n_neighbors=3)
        self.knn_classifier.fit(self.X_train, self.y_train)

    def test_random_forest_model(self):
        # Test if the Random Forest model is trained successfully
        self.assertIsNotNone(self.rf_model)

    def test_knn_classifier(self):
        # Test if the KNN classifier is trained successfully
        self.assertIsNotNone(self.knn_classifier)

    def test_machine_learning_predictions(self):
        # Test the predictions of the Random Forest model
        y_pred_rf = self.rf_model.predict(self.X_test)
        mse_rf = mean_squared_error(self.y_test, y_pred_rf)
        r2_rf = r2_score(self.y_test, y_pred_rf)
        self.assertIsNotNone(y_pred_rf)
        self.assertIsNotNone(mse_rf)
        self.assertIsNotNone(r2_rf)

        # Test the predictions of the KNN classifier
        y_pred_knn = self.knn_classifier.predict(self.X_test)
        self.assertIsNotNone(y_pred_knn)

    def test_visualizations(self):
        # Test if the visualizations are created successfully
        fuel = self.df['Fuel']
        price = self.df['Price']
        sns.barplot(x=fuel, y=price)
        plt.xlabel('Fuel')
        plt.ylabel('Price')
        plt.title('Fuel vs. Price Scatter Plot')
        plt.show()

        owner = self.df['Owner']
        sns.barplot(x=owner, y=price)
        plt.xlabel('Owner')
        plt.ylabel('Price')
        plt.title('Owner vs. Price Scatter Plot')
        plt.show()

        distance = self.df['Distance']
        plt.scatter(distance, price)
        plt.xlabel('Distance')
        plt.ylabel('Price')
        plt.title('Distance vs. Price Scatter Plot')
        plt.show()

        sns.barplot(x='Drive', y='Price', data=self.df)
        plt.xlabel('Driving Type')
        plt.ylabel('Price')
        plt.title('Driving Type vs. Price')
        plt.show()

    def test_data_preprocessing(self):
        # Test if the data preprocessing steps are applied successfully
        self.assertIsNotNone(self.df)

    def test_correlation_heatmap(self):
        # Test if the correlation heatmap is created successfully
        correlation_matrix = self.df.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.show()

if __name__ == '__main__':
    unittest.main()
