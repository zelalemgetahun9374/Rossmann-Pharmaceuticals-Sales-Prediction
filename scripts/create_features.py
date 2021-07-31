import pandas as pd
from config import Config
from sklearn.preprocessing import LabelEncoder

Config.FEATURES_PATH.mkdir(parents=True, exist_ok=True)

train_df = pd.read_csv(str(Config.DATASET_PATH / "train.csv"))
test_df = pd.read_csv(str(Config.DATASET_PATH / "test.csv"))


def extract_features(df):

    # # date
    # df["date"] = pd.to_datetime(df.date).dt.date
    # df["date_of_week"] = pd.to_datetime(df.date).dt.dayofweek

    # since machines understand only numbers change categorical variables to numerical value
    lb = LabelEncoder()
    df['StateHoliday'] = lb.fit_transform(df['StateHoliday'])
    df['Assortment'] = lb.fit_transform(df['Assortment'])
    df['StoreType'] = lb.fit_transform(df['StoreType'])

    return df[['Store','DayOfWeek','Customers','Open',
        'Promo','StateHoliday','SchoolHoliday','Year','Month','DayOfMonth','WeekOfYear',
        'weekday','StoreType','Assortment','CompetitionDistance','CompetitionOpenSinceMonth',
        'CompetitionOpenSinceYear','Promo2','Promo2SinceWeek','Promo2SinceYear',
        'CompetitionBeforeStoreOpened']]


def extract_labels(df):
    return df[["Sales"]]


train_features = extract_features(train_df)
test_features = extract_features(test_df)

train_labels = extract_labels(train_df)
test_labels = extract_labels(test_df)

train_features.to_csv(str(Config.FEATURES_PATH / "train_features.csv"), index=None)
test_features.to_csv(str(Config.FEATURES_PATH / "test_features.csv"), index=None)

train_labels.to_csv(str(Config.FEATURES_PATH / "train_labels.csv"), index=None)
test_labels.to_csv(str(Config.FEATURES_PATH / "test_labels.csv"), index=None)
