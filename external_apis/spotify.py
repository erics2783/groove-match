import requests
import base64
import os
import time

SPOTIFY_API_URL = 'https://api.spotify.com/v1'

class SpotifyAPI:
    def __init__(self):
        self.__token = { 'access_token': None, 'expires_at': None }

    def search(self, query):
        search_url = f'{SPOTIFY_API_URL}/search'
        search_params = {
            'q': query,
            'type': 'album,artist,track',
            'limit': 10
        }
        search_response = requests.get(search_url, headers=self.__get_spotify_headers(), params=search_params)
        search_data = search_response.json()

        return list(map(lambda track: {
            'id': track['id'],
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
        }, search_data['tracks']['items']))


    def get_song_data(self, track_id):
        track_data = self.get_track_data(track_id)
        audio_features = self.get_audio_features(track_id)
        artist_data = self.get_artist_data(track_data['artists'][0]['id'])

        genres = artist_data.get('genres', [])
        
        return track_data, audio_features, genres

    def get_track_data(self, track_id):
        track_url = f'{SPOTIFY_API_URL}/tracks/{track_id}'
        track_response = requests.get(track_url, headers=self.__get_spotify_headers())
        return track_response.json()

    def get_audio_features(self, track_id):
        audio_features_url = f'{SPOTIFY_API_URL}/audio-features/{track_id}'
        audio_features_response = requests.get(audio_features_url, headers=self.__get_spotify_headers())
        return audio_features_response.json()

    def get_artist_data(self, artist_id):
        artist_url = f'{SPOTIFY_API_URL}/artists/{artist_id}'
        artist_response = requests.get(artist_url, headers=self.__get_spotify_headers())
        return artist_response.json()

    def __get_spotify_headers(self):
        access_token = self.__get_access_token()
        return {
            'Authorization': f'Bearer {access_token}'
        }

    def __get_access_token(self):
        # return current access_token if it exists and doesn't expire in the next 10 seconds
        if self.__token['access_token'] is not None and self.__token['expires_at'] > time.time() + 10:
            return self.__token['access_token']

        client_id = os.getenv('SPOTIFY_CLIENT_ID')
        client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

        if not client_id or not client_secret:
            raise Exception('SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET environment variables must be set')

        auth_string = f'{client_id}:{client_secret}'
        auth_bytes = auth_string.encode('utf-8')
        auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')

        token_url = 'https://accounts.spotify.com/api/token'
        headers = {
            'Authorization': f'Basic {auth_base64}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'grant_type': 'client_credentials'
        }

        response = requests.post(token_url, headers=headers, data=data)
        response_data = response.json()
        self.__token = {
            'access_token': response_data.get('access_token'),
            'expires_at': time.time() + response_data.get('expires_in')
        }

        return self.__token['access_token']
