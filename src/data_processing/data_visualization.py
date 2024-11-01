import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualization:
    """Class for visualizing ecosystem data."""
    
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def plot_time_series(self, x: str, y: str):
        """Plot a time series graph."""
        plt.figure(figsize=(12, 6))
        plt.plot(self.data[x], self.data[y], marker='o')
        plt.title(f'Time Series of {y} over {x}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.grid()
        plt.show()

    def plot_scatter(self, x: str, y: str):
        """Plot a scatter plot."""
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.data, x=x, y=y)
        plt.title(f'Scatter Plot of {y} vs {x}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.grid()
        plt.show()

    def plot_correlation_matrix(self):
        """Plot a correlation matrix heatmap."""
        plt.figure(figsize=(12, 8))
        correlation_matrix = self.data.corr()
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
        plt.title('Correlation Matrix')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Load sample data
    data = pd.read_csv('ecosystem_data.csv')
    visualizer = DataVisualization(data)
    visualizer.plot_time_series(x='date ', y='temperature')
    visualizer.plot_scatter(x='humidity', y='temperature')
    visualizer.plot_correlation_matrix()
