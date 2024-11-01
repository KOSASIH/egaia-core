import pandas as pd
import numpy as np

class DataCleaning:
    """Class for cleaning and preprocessing data."""
    
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def handle_missing_values(self, strategy: str = 'mean', columns: list = None):
        """Handle missing values in the dataset."""
        if columns is None:
            columns = self.data.columns.tolist()
        
        for column in columns:
            if strategy == 'mean':
                self.data[column].fillna(self.data[column].mean(), inplace=True)
            elif strategy == 'median':
                self.data[column].fillna(self.data[column].median(), inplace=True)
            elif strategy == 'mode':
                self.data[column].fillna(self.data[column].mode()[0], inplace=True)
            elif strategy == 'drop':
                self.data.dropna(subset=[column], inplace=True)
            else:
                raise ValueError("Unsupported strategy. Choose from 'mean', 'median', 'mode', or 'drop'.")
        print("Missing values handled.")

    def remove_outliers(self, column: str, method: str = 'IQR'):
        """Remove outliers from the dataset based on the specified method."""
        if method == 'IQR':
            Q1 = self.data[column].quantile(0.25)
            Q3 = self.data[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            self.data = self.data[(self.data[column] >= lower_bound) & (self.data[column] <= upper_bound)]
        elif method == 'z-score':
            mean = self.data[column].mean()
            std_dev = self.data[column].std()
            z_scores = (self.data[column] - mean) / std_dev
            self.data = self.data[(z_scores >= -3) & (z_scores <= 3)]
        else:
            raise ValueError("Unsupported method. Choose from 'IQR' or 'z-score'.")
        print("Outliers removed.")

    def normalize_data(self, columns: list):
        """Normalize specified columns in the dataset."""
        for column in columns:
            self.data[column] = (self.data[column] - self.data[column].mean()) / self.data[column].std()
        print("Data normalized.")

# Example usage
if __name__ == "__main__":
    # Load sample data
    data = pd.read_csv('ecosystem_data.csv')
    cleaner = DataCleaning(data)
    cleaner.handle_missing_values(strategy='mean')
    cleaner.remove_outliers(column='temperature', method='IQR')
    cleaner.normalize_data(columns=['temperature', 'humidity'])
