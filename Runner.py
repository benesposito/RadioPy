import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from PyLyrics import *
from credentials import *
from EventHandler import EventHandler

token = util.prompt_for_user_token('espo1234', 'user-library-read user-read-playback-state', client_id=credentials['CLIENT_ID'], client_secret=credentials['CLIENT_SECRET'],redirect_uri='http://localhost:8888/callback')

settings = {
    'showLyrics': True
}

def booleanify(string):
    return string == 'true' or string == 'on' or string == '1'

def onNextTrack():
    currently_playing = sp.currently_playing()

    if currently_playing == None:
        print('None playing')
    else:
        print(PyLyrics.getLyrics(currently_playing['item']['artists'][0]['name'], currently_playing['item']['name']))

def onCommand(args):
    command = args[0]

    if command == 'lyrics':
        settings['showLyrics'] = booleanify(args[1])

if token:
    print('token is good!')
    sp = spotipy.Spotify(auth=token)

    test = EventHandler(sp, onNextTrack, onCommand)
else:
    raise Exception("Can't get token for " + username)
