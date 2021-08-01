from lightgbm import LGBMRegressor
from config import Config
from train_model import TrainModel

# create a model
model = LGBMRegressor()

train_model = TrainModel(model, "Light GBM Regressor")

train_model.train_sales()
train_model.train_customers()