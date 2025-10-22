import numpy as np
import pandas as pd
from pandas._testing import assert_frame_equal


def ZOOtable(zoo: dict) -> pd.DataFrame:
    zoo_table = pd.DataFrame.from_dict(zoo, orient="index")
    zoo_table["Type"] = zoo_table.index
    zoo_table.reset_index(drop=True,inplace=True)
    zoo_table.sort_values("Type", inplace=True)
    zoo_table.dropna(axis=1,inplace=True)
    zoo_table = zoo_table.reindex(sorted(zoo_table.columns), axis=1)
    print(zoo_table)
    return zoo_table

######################################################
ZOO = {
    'cat': {'color': 'black', 'tail_len': 50.0, 'injured': False},
    'dog': {'age': 6, 'tail_len': 30.5, 'injured': True}
}
answer = pd.DataFrame(
    {
        'Type': ['cat', 'dog'],
        'injured': [False, True],
        'tail_len': [50.0, 30.5]
    }
)
df = ZOOtable(ZOO)

assert_frame_equal(
    df.reset_index(drop=True),
    answer
)
######################################################
ZOO = {
    'cat': {'color': 'black'},
    'dog': {'age': 6}
}
answer = pd.DataFrame(
    {
        'Type': ['cat', 'dog']
    }
)

df = ZOOtable(ZOO)

assert_frame_equal(
    df.reset_index(drop=True),
    answer
)
######################################################