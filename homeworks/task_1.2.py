# Задача 1.2.

from random import sample
from datetime import timedelta

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

shuffle_songs = sample(my_favorite_songs, 3)
length = timedelta()
for song, l in shuffle_songs:
    m, s = '{:.2f}'.format(l).split('.')
    ms = timedelta(minutes=int(m), seconds=int(s))
    length += ms
print(f'Три песни звучат {str(length)[2:]}')


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

songs_list = sample(list(my_favorite_songs_dict.items()), 3)
length2 = timedelta()
for song, l in songs_list:
    m, s = '{:.2f}'.format(l).split('.')
    ms = timedelta(minutes=int(m), seconds=int(s))
    length2 += ms
print(f'Три песни звучат {str(length2)[2:]}')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime