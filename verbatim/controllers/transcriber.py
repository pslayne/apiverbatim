from deepspeech import Model
import numpy as np
import os
import wave
import scipy.io.wavfile as wav
from scipy import signal
from pydub import AudioSegment

silence = AudioSegment.silent(500)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

model_file_path = './transcriber models/deepspeech-0.9.3-models.pbmm'
scorer_file_path = './transcriber models/deepspeech-0.9.3-models.scorer'

# hiperparâmetros - valores recomendados
beam_width = 100
scorer_alpha = 0.93
scorer_beta = 1.18

# definindo o modelo
model = Model(model_file_path)
model.enableExternalScorer(scorer_file_path)
model.setScorerAlphaBeta(scorer_alpha, scorer_beta)
model.setBeamWidth(beam_width)


def fix_frame_rate(input_audio_file, output_audio_file):
    # Set the input and output sample rates
    output_sample_rate = 16000  # 16 kHz

    # Read the original audio
    original_sample_rate, audio_data = wav.read(input_audio_file)

    # Resample the audio data
    resampled_audio_data = signal.resample(audio_data, int(len(audio_data) * (output_sample_rate / original_sample_rate)))

    # Save the resampled audio to a new file
    wav.write(output_audio_file, output_sample_rate, resampled_audio_data.astype(np.int16))

def read_wav_file(file):
    input_file = './audio/input.wav'
    output_file = './audio/output.wav'

    sound = AudioSegment.from_wav(file)
    # sound = sound.set_frame_rate(16000) 
    sound = silence + sound + silence
    sound.export(input_file, format="wav")

    fix_frame_rate(input_file, output_file)

    with wave.open(output_file, 'rb') as w:
        rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)
    return buffer, rate

def transcribe_batch(audio_file):
    buffer, rate = read_wav_file(audio_file)
    data16 = np.frombuffer(buffer, dtype=np.int16)
    return model.stt(data16)

