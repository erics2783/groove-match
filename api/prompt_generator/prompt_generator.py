import math
from django.conf import settings
from external_apis.openai_api import OpenAiApi
from external_apis.spotify_api import SpotifyApi

def generate_prompt_from_spotify_track_id(spotify_track_id):
    spotify = SpotifyApi(settings.SPOTIFY['URL'], settings.SPOTIFY['CLIENT_ID'], settings.SPOTIFY['CLIENT_SECRET'])
    track_data = spotify.get_track_data(spotify_track_id)
    if track_data is None:
        return None

    return generate_prompt_from_spotify_track_data(track_data)

def generate_prompt_from_spotify_track_data(spotify_track_data):
    
    track_name = spotify_track_data['name']
    artist = spotify_track_data['artists'][0]['name']
    
    openai = OpenAiApi(settings.OPENAI['API_KEY'])
    return openai.generate_response(
        "User will provide the name of song and artist." +
        " You will then generate a sentence or two prompt designed as input for a text-to-music AI model such as Meta's MusicGen." +
        " Response should be tailored to produce a very similar style, feel, tempo, and time signature as the original song." +
        " Exclude original song name or artist from the response." +
        " Base off of the most recognizable 15 seconds of the song." + 
        " Describe instrumentation, genre and time period." +
        " If you don't know the song, respond with exactly 'I don\'t know that song'." +
        " Respond with only the prompt, no labels or extra info. No vocal or lyric instructions." +
        " 250 characters max.",
        f"{track_name} {artist}",
    )