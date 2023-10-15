from deepspeech import Model
import numpy as np
import os
import wave
import scipy.io.wavfile as wav
from scipy import signal
from pydub import AudioSegment
import speech_recognition as sr

r = sr.Recognizer()

silence = AudioSegment.silent(500)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

def read_wav_file(file):
    audio_file = './audio/audio.wav'
    sound = AudioSegment.from_wav(file)
    sound = silence + sound
    sound.export(audio_file, format="wav")

    with sr.AudioFile(audio_file) as source:
        audio = r.record(source) # read the entire audio file

    return audio

def transcribe_batch(audio_file):
    audio = read_wav_file(audio_file)
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return ''
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

