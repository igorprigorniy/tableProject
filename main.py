import random
import pandas as pd

# Функция создания тестового датафрейма
def createTestDataFrame(rows=1, names_male=[], names_female=[], surnames=[], **kwargs):
    data = []
    for n in range(rows):
        data.append({})

        gender  = random.choice(['male', 'female'])
        name    = random.choice(names_male)  if gender == 'male' else random.choice(names_female)
        surname = random.choice(surnames)[0] if gender == 'male' else random.choice(surnames)[1]

        data[n]['name_cyr']    = name[0]
        data[n]['surname_cyr'] = surname[0]
        data[n]['name_lat']    = name[1]
        data[n]['surname_lat'] = surname[1]
        data[n]['gender']      = gender

        for key, value in kwargs.items():
            data[n][key] = random.choice(value)

    return pd.DataFrame(data)

# Входная точка программы
if __name__ == '__main__':
    df = createTestDataFrame(rows=350, names_male  =[('Василий',  'Vasiliy'   ), ('Иван',     'Ivan'    ), ('Пётр',      'Petr'     ),
                                                     ('Павел',    'Pavel'     ), ('Степан',   'Stepan'  ), ('Алексей',   'Aleksey'  ),
                                                     ('Николай',  'Nikolai'   ), ('Олег',     'Oleg'    ), ('Артём',     'Artem'    ),
                                                     ('Кирилл',   'Kirill'    ), ('Владимир', 'Vladimir'), ('Андрей',    'Andrei'   ),
                                                     ('Семён',    'Semen'     ), ('Дмитрий',  'Dmitriy' ), ('Михаил',    'Mikhail'  )],
                                       names_female=[('Мария',    'Maria'     ), ('Ирина',    'Irina'   ), ('Анастасия', 'Anastasia'),
                                                     ('Анна',     'Anna'      ), ('Варвара',  'Varvara' ), ('Полина',    'Polina'   ),
                                                     ('Ольга',    'Olga'      ), ('Татьяна',  'Tatiana' ), ('Светлана',  'Svetlana' ),
                                                     ('Кристина', 'Kristina'  ), ('Дарья',    'Daria'   ), ('Алёна',     'Alena'    ),
                                                     ('Елизавета', 'Elizaveta'), ('Ксения',   'Ksenia'  ), ('София',     'Sofia'    )],
                                       surnames   =[(('Иванов',    'Ivanov'   ), ('Иванова',    'Ivanova'   )), (('Петров',   'Petrov'),    ('Петрова',   'Petrova'   )),
                                                    (('Сидоров',   'Sidorov'  ), ('Сидорова',   'Sidorova'  )), (('Смирнов',  'Smirnov'),   ('Смирнова',  'Smirnova'  )),
                                                    (('Кузнецов',  'Kuznetsov'), ('Кузнецова',  'Kuznetsova')), (('Соколов',  'Sokolov'),   ('Соколова',  'Sokolova'  )),
                                                    (('Васильев',  'Vasiliev' ), ('Васильева',  'Vasilieva' )), (('Макаров',  'Makarov'),   ('Макарова',  'Makarova'  )),
                                                    (('Соловьёв',  'Solovev'  ), ('Соловьёва',  'Soloveva'  )), (('Беляев',   'Belyaev'),   ('Беляева',   'Belyaeva'  )),
                                                    (('Кузьмин',   'Kuzmin'   ), ('Кузьмина',   'Kuzmina'   )), (('Яковлев',  'Yakovlev'),  ('Яковлева',  'Yakovleva' )),
                                                    (('Романов',   'Romanov'  ), ('Романова',   'Romanova'  )), (('Денисов',  'Denisov'),   ('Денисова',  'Denisova'  )),
                                                    (('Медведев',  'Medvedev' ), ('Медведева',  'Medvedeva' )), (('Поляков',  'Polyakov'),  ('Полякова',  'Polyakova' )),
                                                    (('Жуков',     'Zhukov'   ), ('Жукова',     'Zhukova'   )), (('Филиппов', 'Filippov'),  ('Филиппова', 'Filippova' )),
                                                    (('Тарасов',   'Tarasov'  ), ('Тарасова',   'Tarasova'  )), (('Ефимов',   'Efimov'),    ('Ефимова',   'Efimova'   )),
                                                    (('Мельников', 'Melnikov' ), ('Мельникова', 'Melnikova' )), (('Михайлов', 'Mikhailov'), ('Михайлова', 'Mikhailova'))],
                                       group = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118],
                                       mark1 = [2, 3, 4, 5],
                                       mark2 = [2, 3, 4, 5],
                                       mark3 = [2, 3, 4, 5])
    print(df.head())