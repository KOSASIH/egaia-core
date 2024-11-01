import pandas as pd
import numpy as np
from scipy import stats

class Analytics:
    """Class for statistical analysis."""
    
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def perform_t_test(self, column: str, mu: float):
        """Perform a one-sample t-test."""
        t_stat, p_val = stats.ttest_1samp(self.data[column], mu)
        print(f'T-statistic: {t_stat:.4f}, p-value: {p_val:.4f}')
        if p_val < 0.05:
            print(f'Reject null hypothesis: mean {column} is not equal to {mu}')
        else:
            print(f'Fail to reject null hypothesis: mean {column} is equal to {mu}')

    def calculate_confidence_interval(self, column: str, confidence: float = 0.95):
        """Calculate a confidence interval for a population mean."""
        mean = self.data[column].mean()
        std_dev = self.data[column].std()
        n = len(self.data)
        margin_error = stats.norm.ppf(1 - (1 - confidence) / 2) * std_dev / np.sqrt(n)
        lower_bound = mean - margin_error
        upper_bound = mean + margin_error
        print(f'Confidence Interval ({confidence*100}%): ({lower_bound:.4f}, {upper_bound:.4f})')

    def perform_linear_regression(self, x: str, y: str):
        """Perform linear regression analysis."""
        x_values = self.data[x].values.reshape(-1, 1)
        y_values = self.data[y].values.reshape(-1, 1)
        model = stats.linregress(x_values, y_values)
        print(f'Slope: {model.slope:.4f}, Intercept: {model.intercept:.4f}, R-squared: {model.rvalue**2:.4f}')

# Example usage
if __name__ == "__main__":
    # Load sample data
    data = pd.read_csv('ecosystem_data.csv')
    analyzer = Analytics(data)
    analyzer.perform_t_test(column='temperature', mu=20)
    analyzer.calculate_confidence_interval(column='humidity')
    analyzer.perform_linear_regression(x='humidity', y='temperature')
