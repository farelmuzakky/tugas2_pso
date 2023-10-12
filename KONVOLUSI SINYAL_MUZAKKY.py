# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:53:02 2023

@author: HELIOS 300
"""

def konvolusi(sinyal1, sinyal2):
    #entry sinyal input
    panjang_sinyal1 = len(sinyal1)
    panjang_sinyal2 = len(sinyal2)

    #menginisialisasi array
    hasil = [0] * (panjang_sinyal1 + panjang_sinyal2 - 1)

    #melaakukan konvolusi
    for i in range(panjang_sinyal1):
        for j in range(panjang_sinyal2):
            hasil[i + j] += sinyal1[i] * sinyal2[j]

    return hasil

#eksekusi:
sinyal1 = [1,2,3,4,5]
sinyal2 = [6,7,8,9,10]
hasil_konvolusi = konvolusi(sinyal1, sinyal2)
print("Hasil Konvolusi:", hasil_konvolusi)

import numpy as np

#validasi hasil dengan numpy
hasil_konvolusi_numpy = np.convolve(sinyal1, sinyal2, mode='full')
print("Hasil Konvolusi NumPy:", hasil_konvolusi_numpy)

#periksa apakah hasilnya sama
if np.array_equal(hasil_konvolusi, hasil_konvolusi_numpy):
    print("Hasil sama!")
else:
    print("Hasil tidak sama.")
