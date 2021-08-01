import os
import sys
import pandas as pd
from config import Config
from sklearn.preprocessing import LabelEncoder

sys.path.append(os.path.abspath(os.path.join('../scripts')))
from file_handler import FileHandler

Config.FEATURES_PATH.mkdir(parents=True, exist_ok=True)

def get_part_of_month(day):
    if (day < 10):
      return 0
    elif(day < 20):
      return 1
    else:
      return 2

def extract_features(df):
    df = df[df['Open'] == 1]
    df["part_of_month"] = df["DayOfMonth"].apply(get_part_of_month)

    # since machines understand only numbers change categorical variables to numerical value
    lb = LabelEncoder()
    df['StateHoliday'] = lb.fit_transform(df['StateHoliday'])
    df['Assortment'] = lb.fit_transform(df['Assortment'])
    df['StoreType'] = lb.fit_transform(df['StoreType'])

    df = df.drop(columns=['Sales', 'Customers', 'PromoInterval', 'Date'], axis=1)
    return df

def extract_sales(df):
    df = df[df['Open'] == 1]
    return df[["Sales"]]

def extract_customers(df):
    df = df[df['Open'] == 1]
    return df[["Customers"]]

file_handler = FileHandler()

train_df = file_handler.read_csv(str(Config.DATASET_PATH / "train.csv"))


train_features = extract_features(train_df)

target_sales = extract_sales(train_df)
target_customers = extract_customers(train_df)

train_features.to_csv(str(Config.FEATURES_PATH / "train_features.csv"), index=None)

target_sales.to_csv(str(Config.FEATURES_PATH / "target_sales.csv"), index=None)
target_customers.to_csv(str(Config.FEATURES_PATH / "target_customers.csv"), index=None)
