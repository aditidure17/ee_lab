import numpy as np
import matplotlib.pyplot as plt

# Given values
R = 150e3  # 150 kΩ
C = 220e-12  # 220 pF

# Calculate cutoff frequency
fc = 1 / (2 * np.pi * R * C)

# Define the frequency range
freq = np.logspace(1, 6, 1000)  # 10 Hz to 1 MHz

# Calculate the transfer function
H = 1j * freq / (1j * freq + fc)

# Calculate the gain in decibels
gain_dB = 20 * np.log10(np.abs(H))

# Frequencies to mark
marked_frequencies = [500, 1000, 2000, 4000, 5000, 6000, 10000]

# Plot the graph
plt.figure(figsize=(10, 6))
plt.semilogx(freq, gain_dB, label='Frequency Response')

# Mark specific frequencies
for f in marked_frequencies:
    plt.scatter(f, 20 * np.log10(np.abs(1j * f / (1j * f + fc))), color='blue', marker='o', label=f'{f} Hz')

plt.axhline(y=-3, color='red', linestyle='--', label='-3 dB Point')
plt.title('High-Pass Filter Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.axvline(fc, color='green', linestyle='--', label=f'Cutoff Frequency ({fc:.2f} Hz)')
plt.legend()
plt.grid(True)
plt.savefig('2.png')
plt.show()

