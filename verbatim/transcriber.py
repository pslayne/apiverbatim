from deepspeech import Model
import numpy as np
import os
import wave
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

def read_wav_file(filename):
    with wave.open(filename, 'rb') as w:
        rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)

        # if(rate != 16000):

        print('rate: ', rate)
        print('frames: ', frames)
        print('buffer length: ', len(buffer))
    return buffer, rate

def transcribe_batch(audio_file):
    buffer, rate = read_wav_file(audio_file)
    data16 = np.frombuffer(buffer, dtype=np.int16)
    return model.stt(data16)

print('\n', transcribe_batch('./audio/woman1_wb.wav'))
