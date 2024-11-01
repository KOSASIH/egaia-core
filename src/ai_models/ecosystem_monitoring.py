import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

class EcosystemMonitor:
    """Class for monitoring ecosystem health using machine learning."""
    
    def __init__(self):
        self.model = None
        self.pipeline = None
        self.feature_importances_ = None

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

    def train(self, data: pd.DataFrame, target: str, model_type: str = 'RandomForest', param_grid: Dict = None) -> None:
        """Train the model on the provided data."""
        X, y, preprocessor = self.preprocess_data(data, target)

        # Define the model based on the specified type
        if model_type == 'RandomForest':
            self.model = RandomForestClassifier()
        elif model_type == 'DecisionTree':
            self.model = DecisionTreeClassifier()
        elif model_type == 'SVM':
            self.model = SVC()
        else:
            raise ValueError("Unsupported model type. Choose from 'RandomForest', 'DecisionTree', or 'SVM'.")

        # Create a pipeline
        self.pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                         ('classifier', self.model)])

        # Hyperparameter tuning if param_grid is provided
        if param_grid:
            grid_search = GridSearchCV(self.pipeline, param_grid, cv=5, scoring='accuracy')
            grid_search.fit(X, y)
            self.model = grid_search.best_estimator_
            print(f"Best parameters: {grid_search.best_params_}")
        else:
            # Train the model
            self.pipeline.fit(X, y)

        # Cross-validation score
        cv_scores = cross_val_score(self.pipeline, X, y, cv=5)
        print(f"Cross-Validation Accuracy: {np.mean(cv_scores):.2f} ± {np.std(cv_scores):.2f}")

        # Feature importance
        if hasattr(self.model, 'feature_importances_'):
            self.feature_importances_ = self.model.feature_importances_
            self.plot_feature_importance(X)

    def plot_feature_importance(self, X: pd.DataFrame) -> None:
        """Plot feature importance."""
        if self.feature_importances_ is not None:
            feature_names = np.concatenate([X.select_dtypes(include=['object']).columns, X.select_dtypes(exclude=['object']).columns])
            importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': self.feature_importances_})
            importance_df = importance_df.sort_values(by='Importance', ascending=False)

            plt.figure(figsize=(10, 6))
            sns.barplot(x='Importance', y='Feature', data=importance_df)
            plt.title('Feature Importance')
            plt.show()

    def predict(self, sample: pd.DataFrame) -> str:
        """Predict the health status of an ecosystem based on input features."""
        if self.pipeline is None:
 raise ValueError("Model is not trained. Call the `train` method first.")

        return self.pipeline.predict(sample)[0]

    def evaluate(self, X_test: pd.DataFrame, y_test: pd.Series) -> None:
        """Evaluate the model on the test set."""
        y_pred = self.pipeline.predict(X_test)
        print("Classification Report:")
        print(classification_report(y_test, y_pred))
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))
        print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Example usage
if __name__ == "__main__":
    # Sample data loading
    data = pd.read_csv('ecosystem_data.csv')  # Load your dataset here

    # Initialize the EcosystemMonitor
    monitor = EcosystemMonitor()

    # Train the model
    param_grid = {'classifier__n_estimators': [100, 200, 300], 'classifier__max_depth': [None, 5, 10]}
    monitor.train(data, target='health_status', model_type='RandomForest', param_grid=param_grid)

    # Evaluate the model
    X_test, X_train, y_test, y_train = train_test_split(data.drop(columns=['health_status']), data['health_status'], test_size=0.2, random_state=42)
    monitor.evaluate(X_test, y_test)
