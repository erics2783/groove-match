from external_apis.spotify_api import SpotifyApi
from src import prompt, generate_song

spotify = SpotifyApi()

search_results = spotify.search("Never gonna give you up Rick Astley")

if len(search_results) == 0:
    print("No results found")
    exit()

song = search_results[0]

track_data = spotify.get_track_data(song["id"])
if track_data is None:
    print("No track data found")
    exit()

prompt = prompt.spotify_track_data_to_text_prompt(track_data)

generate_song.generate_song(prompt)

