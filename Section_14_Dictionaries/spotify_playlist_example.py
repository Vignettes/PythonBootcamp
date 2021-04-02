### This exercise is to model how an app like Spotify would order a playlisti in data ###

playlist = {
    'title': 'patagonia bus',
    'author': 'colt steele',
    'songs': [
        {'title': 'turn it off',
         'album': 'no turning back',
         'artist': ['blue'],
         'duration': 2.5
        },
        {
         'title': 'right now',
         'album': 'i mean it',
         'artist': ['red', 'dj bigboi'],  # List inside of the dictionary
         'duration': 5
        },
        {
         'title': 'No',
         'album': 'I said that',
         'artist': ['funkle'],
         'duration': 10
        }
    ]
}


# Let's do some stuff with the data

for song in playlist['songs']: # for each song
    print(song['title']) # print the song name
    
total_length = 0  # To get total length set variable to 0
for song in playlist['songs']: # for each song in the playlist
    total_length += song['duration']  # add the total length to the variable
print(total_length) # print the summed total length
