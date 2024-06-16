import math

SPOTIFY_KEY_VALUE_TO_KEY_NAME = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def spotify_track_data_to_text_prompt(spotify_track_data, spotify_audio_features, genres, match_tempo=True, match_time_signature=True, match_key=True):
    track_name = spotify_track_data['name']
    artist = spotify_track_data['artists'][0]['name']
    tempo = spotify_audio_features['tempo']
    time_signature = spotify_audio_features['time_signature']
    key = spotify_audio_features['key']
    mode = 'major' if spotify_audio_features['mode'] == 1 else 'minor'
    energy = spotify_audio_features['energy']
    danceability = spotify_audio_features['danceability']
    acousticness = spotify_audio_features['acousticness']
    instrumentalness = spotify_audio_features['instrumentalness']
    valence = spotify_audio_features['valence']
    genre_list = ', '.join(genres[0:3]) if genres != None else ''


    print(
        f'Track: {track_name}\n'
        f'Artist: {artist}\n'
        f'Tempo: {tempo} BPM\n'
        f'Time Signature: {time_signature}\n'
        f'Key: {SPOTIFY_KEY_VALUE_TO_KEY_NAME[key]} {mode}\n'
        f'Energy: {energy}\n'
        f'Danceability: {danceability}\n'
        f'Acousticness: {acousticness}\n'
        f'Instrumentalness: {instrumentalness}\n'
        f'Valence: {valence}\n'
        f'Genres: {genre_list}\n'
    )

    mood_description = None
    if (valence > 0.7):
        mood_description = 'happy'
    elif (valence < 0.3):
        mood_description = 'sad'

    prompt = f'A song in the style of "{track_name}" by {artist}, '
    prompt += f'{genre_list}, ' if genre_list != None else ''
    prompt += f'with a tempo of {math.ceil(tempo)} BPM, ' if match_tempo and tempo != None else ''
    prompt += f'in the key of {SPOTIFY_KEY_VALUE_TO_KEY_NAME[key]} {mode}, ' if match_key and key != None else ''
    prompt += f'with {spotify_audio_features["time_signature"]} beats per measure, ' if match_time_signature and time_signature != None else ''
    prompt += f'{"high-energy" if energy > 0.75 else "moderately energetic" if energy > 0.5 else "low-energy"}, ' if energy != None else ''
    prompt += f'danceable rhythm, ' if danceability != None and danceability > 0.5 else ''
    prompt += f'featuring prominent acoustic elements, ' if acousticness != None and acousticness > 0.5 else ''
    prompt += f'instrumental, ' if instrumentalness != None and instrumentalness > 0.5 else ''
    prompt += f'{mood_description} mood, ' if mood_description != None else ''

    return prompt.strip().strip(',')