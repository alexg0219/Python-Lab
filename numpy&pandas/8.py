import numpy as np
import pandas as pd


def men_stat(df: pd.DataFrame) -> (float, float, float, float):
    df = df.loc[df["Sex"] == "male"]
    df = df.loc[df["Survived"] == 0]
    return df["Age"].mean(),df["Age"].median(),df["Age"].max(),df["Age"].min()





df = pd.read_csv('titanic_train.csv', index_col='PassengerId')
print(men_stat(df))