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


#three_songs=my_favorite_songs[ 1 ] [1]+ my_favorite_songs [5] [1]
#if three_songs[1]>60:
    
#m_three_songs=int(three_songs)
#s_three_songs=int((three_songs-m_three_songs)*100)
#print (m_three_songs)
#print (s_three_songs)
#m_three_songs =m_three_songs + s_three_songs//60
#s_three_songs=s_three_songs%60



#print( 'три песни звучат', m_three_songs, 'минут и ', s_three_songs, 'секунд')
#print(datetime.time(three_songs).strftime('%M:%S'))
