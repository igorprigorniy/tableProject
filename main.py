import pandas as pd
import random

# Функция создания тестового датафрейма
def createTestDataFrame(rows=10, **kwargs):

    data = []

    for n in range(rows):
        data.append({})
        for key, value in kwargs.items():
            data[n][key] = random.sample(value, 1)[0]

    return pd.DataFrame(data)

# Входная точка проекта
if __name__ == '__main__':
    df = createTestDataFrame(rows=4, name  = {'Василий', 'Иван', 'Пётр', 'Павел', 'Степан', 'Мария', 'Ирина', 'Анастасия', 'Анна', 'Елизавета'},
                                     group = {101, 102, 103, 104, 105},
                                     mark1 = {2, 3, 4, 5},
                                     mark2 = {2, 3, 4, 5})
    print(df.head())