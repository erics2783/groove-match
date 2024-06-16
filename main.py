from external_apis.spotify import SpotifyAPI
from src import prompt

spotify = SpotifyAPI()

search_results = spotify.search("Never gonna give you up Rick Astley")

if len(search_results) == 0:
    print("No results found")
    exit()

song = search_results[0]

song_data = spotify.get_song_data(song["id"])
if song_data is None:
    print("No song data found")
    exit()

track_data = song_data[0]
audio_features = song_data[1]
genres = song_data[2]

prompt = prompt.spotify_track_data_to_text_prompt(track_data, audio_features, genres)

print("")
print(f"Generating song with prompt: {prompt}")
print("")