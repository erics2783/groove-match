from external_apis.spotify import SpotifyAPI

spotify = SpotifyAPI()

search_results = spotify.search("Never gonna give you up Rick Astley")

if len(search_results) == 0:
    print("No results found")
    exit()

song = search_results[0]

song_data = spotify.get_song_data(song['id'])
if song_data is None:
    print("No song data found")
    exit()

track_data = song_data[0]
audio_features = song_data[1]
genres = song_data[2]


print("")
print(f"{track_data['name']} by {track_data['artists'][0]['name']} (id: {song['id']})")
print("-- audio features --")
print(audio_features)
print("-- genres --")
print(', '.join(genres))
print("")