from sklearn.linear_model import LinearRegression
import pandas as pd
import mlflow
import mlflow.sklearn

X_train = pd.read_csv('../features/train_features.csv', sep=',')
y_train = pd.read_csv('../features/train_labels.csv', sep=',')

mlflow.set_experiment('Linear Regression')
mlflow.sklearn.autolog()
mlflow.log_param('Model', "Linear Regression")
regressor = LinearRegression()
regressor.fit(X_train, y_train)