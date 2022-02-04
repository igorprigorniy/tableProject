import random


names_male = [
    ('Василий', 'Vasiliy'),
    ('Иван', 'Ivan'),
    ('Пётр', 'Petr'),
    ('Павел', 'Pavel'),
    ('Степан', 'Stepan'),
    ('Алексей', 'Aleksey'),
    ('Николай', 'Nikolai'),
    ('Олег', 'Oleg'),
    ('Артём', 'Artem'),
    ('Кирилл', 'Kirill'),
    ('Владимир', 'Vladimir'),
    ('Андрей', 'Andrei'),
    ('Семён', 'Semen'),
    ('Дмитрий', 'Dmitriy'),
    ('Михаил', 'Mikhail')
]

names_female = [
    ('Мария', 'Maria'),
    ('Ирина', 'Irina'),
    ('Анастасия', 'Anastasia'),
    ('Анна', 'Anna'),
    ('Варвара', 'Varvara'),
    ('Полина', 'Polina'),
    ('Ольга', 'Olga'),
    ('Татьяна', 'Tatiana'),
    ('Светлана', 'Svetlana'),
    ('Кристина', 'Kristina'),
    ('Дарья', 'Daria'),
    ('Алёна', 'Alena'),
    ('Елизавета', 'Elizaveta'),
    ('Ксения', 'Ksenia'),
    ('София', 'Sofia')
]

surnames = [
    (('Иванов', 'Ivanov'), ('Иванова', 'Ivanova')),
    (('Петров', 'Petrov'), ('Петрова', 'Petrova')),
    (('Сидоров', 'Sidorov'), ('Сидорова', 'Sidorova')),
    (('Смирнов', 'Smirnov'), ('Смирнова', 'Smirnova')),
    (('Кузнецов', 'Kuznetsov'), ('Кузнецова', 'Kuznetsova')),
    (('Соколов', 'Sokolov'), ('Соколова', 'Sokolova')),
    (('Васильев', 'Vasiliev'), ('Васильева', 'Vasilieva')),
    (('Макаров', 'Makarov'), ('Макарова', 'Makarova')),
    (('Соловьёв', 'Solovev'), ('Соловьёва', 'Soloveva')),
    (('Беляев', 'Belyaev'), ('Беляева', 'Belyaeva')),
    (('Кузьмин', 'Kuzmin'), ('Кузьмина', 'Kuzmina')),
    (('Яковлев', 'Yakovlev'), ('Яковлева', 'Yakovleva')),
    (('Романов', 'Romanov'), ('Романова', 'Romanova')),
    (('Денисов', 'Denisov'), ('Денисова', 'Denisova')),
    (('Медведев', 'Medvedev'), ('Медведева', 'Medvedeva')),
    (('Поляков', 'Polyakov'), ('Полякова', 'Polyakova')),
    (('Жуков', 'Zhukov'), ('Жукова', 'Zhukova')),
    (('Филиппов', 'Filippov'), ('Филиппова', 'Filippova')),
    (('Тарасов', 'Tarasov'), ('Тарасова', 'Tarasova')),
    (('Ефимов', 'Efimov'), ('Ефимова', 'Efimova')),
    (('Мельников', 'Melnikov'), ('Мельникова', 'Melnikova')),
    (('Михайлов', 'Mikhailov'), ('Михайлова', 'Mikhailova'))
]


# Функция создания тестового датафрейма
def create_test_data_frame(count=1):
    rows = []
    for _ in range(count):
        gender = random.choice(['male', 'female'])
        name = random.choice(names_male) if gender == 'male' else random.choice(names_female)
        surname = random.choice(surnames)[0] if gender == 'male' else random.choice(surnames)[1]
        rows.append((
            name[0],
            surname[0],
            ' '.join([name[0], surname[0]]),
            name[1],
            surname[1],
            ' '.join([name[1], surname[1]]),
            gender
        ))

    return rows


def main():
    arr = create_test_data_frame(count=20)

    for item in arr:
        print(item)


# Входная точка программы
if __name__ == '__main__':
    main()
