import unittest
import pandas as pd
from data_processing import DataCleaning  # Assuming DataCleaning is in data_processing.py

class TestDataProcessing(unittest.TestCase):
    """Unit tests for data processing functions."""

    def setUp(self):
        # Sample data for testing
        self.data = pd.DataFrame({
            'temperature': [22, 23, None, 25, 30, 100],
            'humidity': [30, 35, 40, None, 50, 60]
        })
        self.cleaner = DataCleaning(self.data)

    def test_handle_missing_values(self):
        # Test handling of missing values
        self.cleaner.handle_missing_values(strategy='mean')
        self.assertFalse(self.cleaner.data['temperature'].isnull().any())

    def test_remove_outliers(self):
        # Test removal of outliers
        self.cleaner.remove_outliers(column='temperature', method='IQR')
        self.assertNotIn(100, self.cleaner.data['temperature'].values)

if __name__ == "__main__":
    unittest.main()
