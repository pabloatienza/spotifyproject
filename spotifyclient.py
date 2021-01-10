import json

import requests

from track import Track
from playlist import Playlist
from preset import Preset

import secretCredentials
import preset

#from PIL import Image
#import base64


class SpotifyClient:
    """SpotifyClient performs operations using the Spotify API."""

    def __init__(self, authorization_token, user_id):
        """
        :param authorization_token (str): Spotify API token
        :param user_id (str): Spotify user id
        """
        self._authorization_token = secretCredentials.access_token
        self._user_id = secretCredentials.User_ID

    def get_last_played_tracks(self, limit=10):
        """Get the last n tracks played by a user
        :param limit (int): Number of tracks to get. Should be <= 50
        :return tracks (list of Track): List of last played tracks
        """
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()

        ####
        tracks = []

        for track in response_json['items']:
            trackid = track['track']['id']
            features = self._place_get_api_request(f'https://api.spotify.com/v1/audio-features/{trackid}')
            features_json = features.json()

            fulltrack = Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"],
                              features_json['tempo'], features_json['acousticness'], features_json['danceability'],
                              features_json['energy'], features_json['valence'])

            tracks.append(fulltrack)
        return tracks

        ####
        #tracks = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for
        #          track in response_json["items"]]
        #return tracks

        # custom
    def get_top_tracks_long(self, limit=10):
        """Get the top n tracks played by a user in the long term
        :param limit (int): Number of tracks to get. Should be <= 50
        :return tracks (list of Track): List of last played tracks
        """
        url = f"https://api.spotify.com/v1/me/top/tracks?time_range=long_term&limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        tracks = []
        for track in response_json['items']:
            trackid = track['id']
            features = self._place_get_api_request(f'https://api.spotify.com/v1/audio-features/{trackid}')
            features_json = features.json()

            fulltrack = Track(track["name"], track["id"], track["artists"][0]["name"],
                              features_json['tempo'], features_json['acousticness'], features_json['danceability'],
                              features_json['energy'], features_json['valence'])

            tracks.append(fulltrack)
        return tracks

    #custom
    def get_top_tracks_medium(self, limit=10):
        """Get the top n tracks played by a user in the medium term
        :param limit (int): Number of tracks to get. Should be <= 50
        :return tracks (list of Track): List of last played tracks
        """
        url = f"https://api.spotify.com/v1/me/top/tracks?time_range=medium_term&limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        tracks=[]
        for track in response_json['items']:
            trackid = track['id']
            features = self._place_get_api_request(f'https://api.spotify.com/v1/audio-features/{trackid}')
            features_json = features.json()

            fulltrack = Track(track["name"], track["id"], track["artists"][0]["name"],
                              features_json['tempo'], features_json['acousticness'], features_json['danceability'],
                              features_json['energy'], features_json['valence'])

            tracks.append(fulltrack)
        return tracks

    #custom
    def get_top_tracks_short(self, limit=10):
        """Get the top n tracks played by a user in the short term
        :param limit (int): Number of tracks to get. Should be <= 50
        :return tracks (list of Track): List of last played tracks
        """
        url = f"https://api.spotify.com/v1/me/top/tracks?time_range=short_term&limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        tracks=[]
        for track in response_json['items']:
            trackid = track['id']
            features = self._place_get_api_request(f'https://api.spotify.com/v1/audio-features/{trackid}')
            features_json = features.json()

            fulltrack = Track(track["name"], track["id"], track["artists"][0]["name"],
                              features_json['tempo'], features_json['acousticness'], features_json['danceability'],
                              features_json['energy'], features_json['valence'])

            tracks.append(fulltrack)
        return tracks

    def get_track_recommendations(self, seed_tracks, limit=50):
        """Get a list of recommended tracks starting from a number of seed tracks.
        :param seed_tracks (list of Track): Reference tracks to get recommendations. Should be 5 or less.
        :param limit (int): Number of recommended tracks to be returned
        :return tracks (list of Track): List of recommended tracks
        """
        seed_tracks_url = ""
        for seed_track in seed_tracks:
            seed_tracks_url += seed_track.id + ","
        seed_tracks_url = seed_tracks_url[:-1]
        url = f"https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks_url}&limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()

        tracks = []
        for track in response_json['tracks']:
            trackid = track['id']
            features = self._place_get_api_request(f'https://api.spotify.com/v1/audio-features/{trackid}')
            features_json = features.json()

            fulltrack = Track(track["name"], track["id"], track["artists"][0]["name"],
                              features_json['tempo'], features_json['acousticness'], features_json['danceability'],
                              features_json['energy'], features_json['valence'])

            tracks.append(fulltrack)
        return tracks

        #tracks = [Track(track["name"], track["id"], track["artists"][0]["name"]) for
        #          track in response_json["tracks"]]
        #return tracks

    #def filter_tracks(self, tracks, bpmmin=0, bpmmax=2000, acmin=0, acmax=1, ):

    def get_track_recommendations_custom(self, seed_tracks, limit=50, bpmtarget=None, bpmmin=0, bpmmax=2000,
                                          acmin=0.0, acmax=1.0, dancemin=0.0, dancemax=1.0,
                                          energymin=0.0, energymax=1.0, valenmin=0.0, valenmax=1.0):
        """Get a list of recommended tracks starting from a number of seed tracks.
        :param seed_tracks (list of Track): Reference tracks to get recommendations. Should be 5 or less.
        :param limit (int): Number of recommended tracks to be returned
        :return tracks (list of Track): List of recommended tracks
        """
        seed_tracks_url = ""
        for seed_track in seed_tracks:
            seed_tracks_url += seed_track.id + ","
        seed_tracks_url = seed_tracks_url[:-1]
        url = f"https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks_url}&limit={limit}" \
              f"&min_acousticness={acmin}&max_acousticness={acmax}&min_danceability={dancemin}" \
              f"&max_danceability={dancemax}&min_energy={energymin}&max_energy={energymax}" \
              f"&min_tempo={bpmmin}&max_tempo={bpmmax}&target_tempo={bpmtarget}" \
              f"&min_valence={valenmin}&max_valence={valenmax}"
        response = self._place_get_api_request(url)
        response_json = response.json()

        tracks = []
        for track in response_json['tracks']:
            trackid = track['id']
            features = self._place_get_api_request(f'https://api.spotify.com/v1/audio-features/{trackid}')
            features_json = features.json()

            fulltrack = Track(track["name"], track["id"], track["artists"][0]["name"],
                              features_json['tempo'], features_json['acousticness'], features_json['danceability'],
                              features_json['energy'], features_json['valence'])

            tracks.append(fulltrack)
        return tracks

    def get_track_recommendations_presets(self, seed_tracks, preset, limit=50):
        """Get a list of recommended tracks starting from a number of seed tracks.
        :param seed_tracks (list of Track): Reference tracks to get recommendations. Should be 5 or less.
        :param preset: preset values to filter the track recommendations
        :param limit (int): Number of recommended tracks to be returned
        :return tracks (list of Track): List of recommended tracks
        """
        seed_tracks_url = ""
        for seed_track in seed_tracks:
            seed_tracks_url += seed_track.id + ","
        seed_tracks_url = seed_tracks_url[:-1]
        url = f"https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks_url}&limit={limit}" \
              f"&min_acousticness={preset.acmin}&max_acousticness={preset.acmax}&min_danceability={preset.dancemin}" \
              f"&max_danceability={preset.dancemax}&min_energy={preset.energymin}&max_energy={preset.energymax}" \
              f"&min_tempo={preset.bpmmin}&max_tempo={preset.bpmmax}&target_tempo={preset.bpmtarget}" \
              f"&min_valence={preset.valenmin}&max_valence={preset.valenmax}"
        response = self._place_get_api_request(url)
        response_json = response.json()

        tracks = []
        for track in response_json['tracks']:
            trackid = track['id']
            features = self._place_get_api_request(f'https://api.spotify.com/v1/audio-features/{trackid}')
            features_json = features.json()

            fulltrack = Track(track["name"], track["id"], track["artists"][0]["name"],
                              features_json['tempo'], features_json['acousticness'], features_json['danceability'],
                              features_json['energy'], features_json['valence'])

            tracks.append(fulltrack)
        return tracks

    def choose_presets(self):
        preset.presets_list()
        select = int(input('\nChoose an option: '))
        selection = preset.presets[(select-1)]
        return selection

    def create_playlist(self, name):
        """
        :param name (str): New playlist name
        :return playlist (Playlist): Newly created playlist
        """
        data = json.dumps({
            "name": name,
            "description": "Recommended songs",
            "public": True
        })
        url = f"https://api.spotify.com/v1/users/{self._user_id}/playlists"
        response = self._place_post_api_request(url, data)
        response_json = response.json()

        # create playlist
        playlist_id = response_json["id"]
        playlist = Playlist(name, playlist_id)
        return playlist

    def populate_playlist(self, playlist, tracks):
        """Add tracks to a playlist.
        :param playlist (Playlist): Playlist to which to add tracks
        :param tracks (list of Track): Tracks to be added to playlist
        :return response: API response
        """
        track_uris = [track.create_spotify_uri() for track in tracks]
        data = json.dumps(track_uris)
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"
        response = self._place_post_api_request(url, data)
        response_json = response.json()
        return response_json

    #def playlist_cover(self, playlist):
    #    #img = Image.open('gradient300.jpg')
    #    with open("gradient300.jpg", "rb") as image_file:
    #        img = base64.b64encode(image_file.read())
    #    url = f'https://api.spotify.com/v1/playlists/{playlist.id}/images'
    #    self._place_put_api_request_image(url, img)


    def _place_get_api_request(self, url):
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._authorization_token}"
            }
        )
        return response

    def _place_post_api_request(self, url, data):
        response = requests.post(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._authorization_token}"
            }
        )
        return response

    #def _place_put_api_request_image(self, url, data):
    #    response = requests.post(
    #        url,
    #        data=data,
    #        headers={
    #            "Content-Type": "image/jpeg",
    #            "Authorization": f"Bearer {self._authorization_token}"
    #        }
    #    )
    #    return response