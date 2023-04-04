import random
import math
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

random_songs = (random.sample(my_favorite_songs, 3))
print(random_songs)
n=random_songs[0][1]+random_songs[1][1]
n_int=int(n)
n_float=n-n_int
if n_float>=0.60:
    n_int=n_int+1
    n_float=n_float-0.60
n=round(n_int+n_float,2)
n=n+random_songs[2][1]
n_int=int(n)
n_float=n-n_int
if n_float>=0.60:
    n_int=n_int+1
    n_float=n_float-0.60
n=round(n_int+n_float,2)

print('Три песни звучат', n, 'минут')

# Ну довольно громоздко) но да, так можно)
# вот например мое решение
from datetime import timedelta
from math import modf
from random import sample


total_time = timedelta()

for song in sample(my_favorite_songs, 3):
    s, m = modf(song[1])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))

print(f'Три песни звучат {total_time} минут')
