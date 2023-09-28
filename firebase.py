
import environ
env = environ.Env()
environ.Env.read_env('.env')

from firebase_admin import credentials, initialize_app, storage

cred = credentials.Certificate("verbatim-d3d61-firebase-adminsdk-ov20t-a98cc9e9af.json")
firebase = initialize_app(cred, 
                          {'storageBucket': 'verbatim-d3d61.appspot.com'})
bucket = storage.bucket()
blob = bucket.blob('audio/woman1_wb.wav')
blob.upload_from_filename('audio/woman1_wb.wav')

# Opt : if you want to make public access from the URL
# blob.make_public()

blob.download_to_filename('audio/test.wav')

print("your file url", blob.public_url)


