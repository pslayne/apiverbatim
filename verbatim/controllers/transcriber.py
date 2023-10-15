import numpy as np
import os
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
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return ''
