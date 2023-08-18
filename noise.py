import librosa
import librosa as librosa
import librosa.effects
import numpy as np
import soundfile as sf
import os

path_list = ['D:/Универ/НИР/Phrase_1_16/78/20.03.2017']
path2_list = ['D:/Универ/НИР/Phrase_de_noise/78/20.03.2017']



def de_noise():
        i = 0
        for path in path_list:
                for filename in os.listdir(path):
                        f = os.path.join(path, filename)
                        if os.path.isfile(f) and filename.endswith('.wav'):
                                audio, sr = librosa.load(f'{f}')
                                spec = librosa.feature.melspectrogram(y=audio, sr=sr)
                                spec_mean = librosa.feature.melspectrogram(y=audio, sr=sr).mean(axis=1)
                                spec_mean = spec_mean.reshape((-1, 1))
                                spec -= spec_mean
                                audio_denoised = librosa.feature.inverse.mel_to_audio(spec)

                                sf.write(f'{path2_list[i]}/{filename}.wav', audio_denoised, sr)
        i += 1

de_noise()