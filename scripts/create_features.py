import os
import sys
import pandas as pd
from config import Config
from sklearn.preprocessing import LabelEncoder

sys.path.append(os.path.abspath(os.path.join('../scripts')))
from file_handler import FileHandler

Config.FEATURES_PATH.mkdir(parents=True, exist_ok=True)

file_handler = FileHandler()

train_df = file_handler.read_csv(str(Config.DATASET_PATH / "train.csv"))
test_df = file_handler.read_csv(str(Config.DATASET_PATH / "test.csv"))
store_df = file_handler.read_csv(str(Config.DATASET_PATH / "store.csv"))

def merge(df, store):
    df_merge = pd.merge(df, store, on='Store')
    return df_merge

def get_part_of_month(day):
    if (day < 10):
      return 0
    elif(day < 20):
      return 1
    else:
      return 2

def extract_test_features(df):
    df = merge(df, store_df)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].apply(lambda x: x.year)
    df['Month'] = df['Date'].apply(lambda x: x.month)
    df['DayOfMonth'] = df['Date'].apply(lambda x: x.day)
    df['WeekOfYear'] = df['Date'].apply(lambda x: x.weekofyear)
    df['weekday'] = df['DayOfWeek'].apply(lambda x: 0 if (x in [6, 7]) else 1)

    df = df[df['Open'] == 1]
    df["part_of_month"] = df["DayOfMonth"].apply(get_part_of_month)

    # since machines understand only numbers change categorical variables to numerical value
    lb = LabelEncoder()
    df['StateHoliday'] = lb.fit_transform(df['StateHoliday'])
    df['Assortment'] = lb.fit_transform(df['Assortment'])
    df['StoreType'] = lb.fit_transform(df['StoreType'])

    df = df.drop(columns=['Id', 'PromoInterval', 'Date'], axis=1)
    return df

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


train_features = extract_features(train_df)
test_features = extract_test_features(test_df)

target_sales = extract_sales(train_df)
target_customers = extract_customers(train_df)

train_features.to_csv(str(Config.FEATURES_PATH / "train_features.csv"), index=None)
test_features.to_csv(str(Config.FEATURES_PATH / "test_features.csv"), index=None)

target_sales.to_csv(str(Config.FEATURES_PATH / "target_sales.csv"), index=None)
target_customers.to_csv(str(Config.FEATURES_PATH / "target_customers.csv"), index=None)
