import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

class PredictiveModel:
    """Class for predicting ecosystem responses using various regression models."""
    
    def __init__(self):
        self.model = None
        self.pipeline = None

    def preprocess_data(self, data: pd.DataFrame, target: str) -> Tuple[pd.DataFrame, pd.Series]:
        """Preprocess the data: handle missing values, scale features, and encode categorical variables."""
        # Fill missing values
        data.fillna(data.mean(), inplace=True)

        # Separate features and target
        X = data.drop(columns=[target])
        y = data[target]

        # Identify categorical and numerical columns
        categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
        numerical_cols = X.select_dtypes(exclude=['object']).columns.tolist()

        # Create a column transformer for preprocessing
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_cols),
                ('cat', OneHotEncoder(), categorical_cols)
            ]
        )

        return X, y, preprocessor

    def train(self, data: pd.DataFrame, target: str, model_type: str = 'LinearRegression', param_grid: Dict = None) -> None:
        """Train the model on the provided data."""
        X, y, preprocessor = self.preprocess_data(data, target)

        # Define the model based on the specified type
        if model_type == 'LinearRegression':
            self.model = LinearRegression()
        elif model_type == 'RandomForest':
            self.model = RandomForestRegressor()
        elif model_type == 'SVR':
            self.model = SVR()
        else:
            raise ValueError("Unsupported model type. Choose from 'LinearRegression', 'RandomForest', or 'SVR'.")

        # Create a pipeline
        self.pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                         ('regressor', self.model)])

        # Hyperparameter tuning if param_grid is provided
        if param_grid:
            grid_search = GridSearchCV(self.pipeline, param_grid, cv=5, scoring='neg_mean_squared_error')
            grid_search.fit(X, y)
            self.model = grid_search.best_estimator_
            print(f"Best parameters: {grid_search.best_params_}")
        else:
            # Train the model
            self.pipeline.fit(X, y)

        # Cross-validation score
        cv_scores = cross_val_score(self.pipeline, X, y, cv=5, scoring='neg_mean_squared_error')
        print(f"Cross-Validation MSE: {-np.mean(cv_scores):.2f} ± {np.std(cv_scores):.2f}")

    def predict(self, sample: pd.DataFrame) -> float:
        """Predict the ecosystem response based on input features."""
        if self.pipeline is None:
            raise ValueError("Model is not trained. Call the `train` method first.")

        return self.pipeline.predict(sample)[0]

    def evaluate(self, X_test: pd.DataFrame, y_test: pd.Series) -> None:
        """Evaluate the model on the test set."""
        y_pred = self.pipeline.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        print(f"Mean Absolute Error: {mae:.2f}")
        print(f"Mean Squared Error: {mse:.2f}")
        print(f"R-squared: {r2:.2f}")

        # Visualization of predictions vs actual values
        plt.figure(figsize=(10,  6))
        plt.scatter(y_test, y_pred)
        plt.xlabel('Actual Values')
        plt.ylabel('Predicted Values')
        plt.title('Predictions vs Actual Values')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Sample data loading
    data = pd.read_csv('ecosystem_data.csv')  # Load your dataset here

    # Initialize the PredictiveModel
    model = PredictiveModel()

    # Train the model
    param_grid = {'regressor__n_estimators': [100, 200, 300], 'regressor__max_depth': [None, 5, 10]}
    model.train(data, target='response_variable', model_type='RandomForest', param_grid=param_grid)

    # Evaluate the model
    X_test, X_train, y_test, y_train = train_test_split(data.drop(columns=['response_variable']), data['response_variable'], test_size=0.2, random_state=42)
    model.evaluate(X_test, y_test)
