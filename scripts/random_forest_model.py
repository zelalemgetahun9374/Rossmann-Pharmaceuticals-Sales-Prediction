from sklearn.ensemble import RandomForestRegressor
from config import Config
from train_model import TrainModel

# create a model
model = RandomForestRegressor(n_jobs=-1, n_estimators=15)

train_model = TrainModel(model, "Random Forest Regressor")

train_model.train_sales()
train_model.train_customers()