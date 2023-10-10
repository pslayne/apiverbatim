
import environ
env = environ.Env()
environ.Env.read_env('.env')

from firebase_admin import credentials, initialize_app, storage

_bucket = 0

def init_firebase():
  cred = credentials.Certificate("./verbatim-d3d61-firebase-adminsdk-ov20t-a98cc9e9af.json")
  initialize_app(cred, {'storageBucket': 'verbatim-d3d61.appspot.com'})
  global _bucket
  _bucket = storage.bucket()

init_firebase()
def get_bucket():
  return _bucket




