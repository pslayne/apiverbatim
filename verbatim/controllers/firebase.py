
import environ
env = environ.Env()
environ.Env.read_env('.env')

from firebase_admin import credentials, initialize_app, storage

def init_firebase():
  cred = credentials.Certificate("./verbatim-d3d61-firebase-adminsdk-ov20t-a98cc9e9af.json")
  initialize_app(cred, 
                            {'storageBucket': 'verbatim-d3d61.appspot.com'})
  return storage.bucket()




