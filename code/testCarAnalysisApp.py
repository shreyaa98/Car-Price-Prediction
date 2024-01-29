# Import libraries
import pandas as pd
import pytest
from unittest.mock import patch
from carAnalysisApp import CarAnalysis

# Mock DataFrame for testing
mock_data = {
    'Car Name': ['Car1', 'Car2', 'Car3', 'Car4'],
    'Drive': ['Manual', 'Automatic', 'Manual', 'Automatic'],
    'Type': ['SUV', 'Sedan', 'SUV', 'Hatchback'],
    'Owner': ['John', 'Jane', 'John', 'Bob'],
    'Distance': [100, 200, 150, 120],
    'Price': [30000, 25000, 35000, 20000]
}

mock_df = pd.DataFrame(mock_data)

# Mock file_path for testing
mock_file_path = 'cars_24_combined.csv'


def test_calculate_correlation_heatmap():
    analysis = CarAnalysis(mock_df)
    correlation_matrix = analysis.calculate_correlation_heatmap()

    # Perform assertions on the correlation matrix
    assert isinstance(correlation_matrix, pd.DataFrame)
    assert correlation_matrix.shape == (2, 2)  # Adjust the shape according to your actual DataFrame

# Method to display top 5 car types in a label
def test_get_top_5_car_types():
    analysis = CarAnalysis(mock_df)
    top_5_car_types = analysis.get_top_5_car_types()

    # Perform assertions on the top 5 car types DataFrame
    assert isinstance(top_5_car_types, pd.DataFrame)
    assert top_5_car_types.shape == (4, 3)  # Adjust the shape according to your actual DataFrame

 # Method to plot a bar chart for Owner vs. Price
def test_get_owner_vs_price_data():
    analysis = CarAnalysis(mock_df)
    owner_vs_price_data = analysis.get_owner_vs_price_data()

    # Perform assertions on the owner vs. price DataFrame
    assert isinstance(owner_vs_price_data, pd.DataFrame)
    assert owner_vs_price_data.shape == (4, 2)  # Adjust the shape according to your actual DataFrame

# Method to plot a bar chart for distance vs. Price
def test_get_distance_vs_price_data():
    analysis = CarAnalysis(mock_df)
    distance_vs_price_data = analysis.get_distance_vs_price_data()

    # Perform assertions on the distance vs. price DataFrame
    assert isinstance(distance_vs_price_data, pd.DataFrame)
    assert distance_vs_price_data.shape == (4, 2)  # Adjust the shape according to your actual DataFrame

# Method to plot a bar chart for Driving type vs. Price
def test_get_driving_type_vs_price_data():
    analysis = CarAnalysis(mock_df)
    driving_type_vs_price_data = analysis.get_driving_type_vs_price_data()

    # Perform assertions on the driving type vs. price DataFrame
    assert isinstance(driving_type_vs_price_data, pd.DataFrame)
    assert driving_type_vs_price_data.shape == (4, 2)  # Adjust the shape according to your actual DataFrame


if __name__ == '__main__':
    pytest.main(['testCarAnalysisApp.py','carAnalysisApp'])
