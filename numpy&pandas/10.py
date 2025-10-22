import pandas as pd

def get_name(info):
    list_info = info.split(" ")

    if "Miss." in list_info:
        return list_info[list_info.index("Miss.")+1]
    else:
        return pd.NA

def fename_stat(df: pd.DataFrame) -> pd.DataFrame:
    df = df.loc[df["Sex"] == "female"]
    name_table = df["Name"].apply(get_name)
    name_table.dropna(axis=0,inplace=True)
    name_table = name_table.value_counts()
    name_table = name_table.to_frame("Popularity")
    name_table = name_table.sort_values(["Popularity", "Name"], ascending = (False , True))
    name_table.reset_index(inplace=True)
    print(name_table.head(10))
    return name_table


df = pd.read_csv('titanic_train.csv', index_col='PassengerId')
fename_stat(df)