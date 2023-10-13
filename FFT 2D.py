import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 256)
y = np.linspace(0, 1, 256)
X, Y = np.meshgrid(x, y)
signal = np.sin(20 * np.pi * X) + np.sin(10 * np.pi * Y)

fft_signal = np.fft.fft2(signal)
fft_signal = np.fft.fftshift(fft_signal)

magnitude_spectrum = np.abs(fft_signal)

plt.figure(figsize=(8, 8))
plt.subplot(121)
plt.imshow(signal, cmap='gray')
plt.title('Gambar Asli')

plt.subplot(122)
plt.imshow(np.log(1 + magnitude_spectrum), cmap='gray')
plt.title('Spektrum Frekuensi (log-scaled)')

plt.show()
