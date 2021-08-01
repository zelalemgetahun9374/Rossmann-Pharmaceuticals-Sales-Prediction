from sklearn.linear_model import LinearRegression
from config import Config
from train_model import TrainModel

# create a model
model = LinearRegression()

train_model = TrainModel(model, "Linear Regression")

train_model.train_sales()
train_model.train_customers()