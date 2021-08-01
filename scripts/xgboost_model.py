from xgboost import XGBRegressor
from config import Config
from train_model import TrainModel

# create a model
model = XGBRegressor()

train_model = TrainModel(model, "XGB Regressor")

train_model.train_sales()
train_model.train_customers()