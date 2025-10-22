import datetime

import dateutil
import numpy as np
import pandas as pd
from pandas._testing import assert_frame_equal

month_in_num = {
    "января": 1,
    "февраля": 2,
    "марта": 3,
    "апреля": 4,
    "мая": 5,
    "июня": 6,
    "июля": 7,
    "августа": 8,
    "сентября": 9,
    "октября": 10,
    "ноября": 11,
    "декабря": 12,
}

def time_delta(str):
    list_number = str.replace("г.", " ").split(" ")
    date_first = datetime.date(int(list_number[2]), month_in_num.get(list_number[1]), int(list_number[0]))
    date_second = datetime.date(int(list_number[6]), month_in_num.get(list_number[5]), int(list_number[4]))
    difference_in_years = dateutil.relativedelta.relativedelta(date_first, date_second).years
    #print(difference_in_years)
    return difference_in_years

def rus_feature(df: pd.DataFrame) -> pd.DataFrame:
    data = df["Дата смерти"] + df["Дата рождения"]
    #data = data.apply(time_delta)
    df["Полных лет"] = data.apply(time_delta)
    print(df)
    return df



names = pd.DataFrame({'Имя': ['Никола Тесла', 'Альберт Эйнштейн'],
                      'Дата рождения': ['10 июля 1856 г.', '14 марта 1879 г.'],
                      'Дата смерти':  ['7 января 1943 г.', '18 апреля 1955 г.']})
answer = pd.DataFrame({'Имя': ['Никола Тесла', 'Альберт Эйнштейн'],
                       'Дата рождения': ['10 июля 1856 г.', '14 марта 1879 г.'],
                       'Дата смерти':  ['7 января 1943 г.', '18 апреля 1955 г.'],
                       'Полных лет': [86, 76]})
assert_frame_equal(
    rus_feature(names),
    answer
)
######################################################
names = pd.DataFrame({'Имя': ['Никола Тесла'],
                      'Дата рождения': ['10 июля 1856 г.'],
                      'Дата смерти':  ['7 января 1857 г.']})
answer = pd.DataFrame({'Имя': ['Никола Тесла'],
                       'Дата рождения': ['10 июля 1856 г.'],
                       'Дата смерти':  ['7 января 1857 г.'],
                       'Полных лет': [0]})
assert_frame_equal(
    rus_feature(names),
    answer
)
######################################################
names = pd.DataFrame({'Имя': ['Никола Тесла'],
                      'Дата рождения': ['1 января 2000 г.'],
                      'Дата смерти':  ['31 декабря 2000 г.']})
answer = pd.DataFrame({'Имя': ['Никола Тесла'],
                       'Дата рождения': ['1 января 2000 г.'],
                       'Дата смерти':  ['31 декабря 2000 г.'],
                       'Полных лет': [0]})
assert_frame_equal(
    rus_feature(names),
    answer
)