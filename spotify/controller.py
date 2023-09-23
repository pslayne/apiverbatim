import environ
import requests

env = environ.Env()
environ.Env.read_env('./.env')

def getAccessToken():
    url = 'https://accounts.spotify.com/api/token'
    body = {
        'grant_type': 'client_credentials', 
        'client_id': env('SPOTIFY_CLIENT_ID'),
        'client_secret': env('SPOTIFY_CLIENT_SECRET')
    }
    header = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, body, header)
    return response.json()['access_token']
