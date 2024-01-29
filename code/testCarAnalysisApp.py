# Import libraries
import pandas as pd
import pytest
from unittest.mock import patch
from carAnalysisApp import CarAnalysis  # Check this import

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

# Rest of the code remains the same...


