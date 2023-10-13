# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 19:57:13 2023

@author: HELIOS 300
"""

import librosa
import librosa.display
import matplotlib.pyplot as plt

# Baca file audio
audio_file = "D:/MOVIE/atambut.wav"
y, sr = librosa.load(audio_file)

# Hitung MFCC
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

# Tampilkan grafik MFCC
plt.figure(figsize=(10, 6))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('MFCC')
plt.show()
