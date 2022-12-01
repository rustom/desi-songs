import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

# playlists = sp.user_playlists('shidoarichimorin')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None
        
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
all_genres = {}
for idx, item in enumerate(results['items']):
    print(item['track']['artists'][0]['uri'])
    artist_uri = item['track']['artists'][0]['uri']
    genres = sp.artist(artist_uri)['genres']
    print(genres)
    track = item['track']
    # print(idx, track['artists'][0]['name'], " – ", track['name'])