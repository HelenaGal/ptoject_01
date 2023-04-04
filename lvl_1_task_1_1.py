my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

print((my_favorite_songs.split(","))[0])
print((my_favorite_songs.split(","))[len((my_favorite_songs.split(",")))-1])
print((my_favorite_songs.split(","))[1])
print((my_favorite_songs.split(","))[len(my_favorite_songs.split(","))-2])

# Отлино) но в приницпе достаточно и одного сплита

songs = my_favorite_songs.split(', ')

print(songs[0], songs[-1], songs[1], songs[-2])
