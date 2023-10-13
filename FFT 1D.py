# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:42:09 2023

@author: HELIOS 300
"""

import cmath
import matplotlib.pyplot as plt

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

# Contoh sinyal 1D
signal = [0, 1, 0, -1, 0, 1, 0, -1]

# Melakukan FFT pada sinyal
spectrum = fft(signal)

# Menghitung magnitude spektrum
magnitude_spectrum = [abs(x) for x in spectrum]

# Membuat plot
plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.plot(signal)
plt.title("Sinyal Asli")
plt.subplot(122)
plt.plot(magnitude_spectrum)
plt.title("Spektrum Magnitude")
plt.tight_layout()
plt.show()
