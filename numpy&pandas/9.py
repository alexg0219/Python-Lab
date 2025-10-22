import pandas as pd

def age_stat(df: pd.DataFrame) -> pd.DataFrame:
    df = df.pivot_table(index=["Sex", "Pclass"],values=["Age"], aggfunc="median")
    return df


df = pd.read_csv('titanic_train.csv', index_col='PassengerId')
print(age_stat(df))
