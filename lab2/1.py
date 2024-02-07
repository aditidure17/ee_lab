import numpy as np
import matplotlib.pyplot as plt

# Given values
V = 5  # Voltage (in volts)
R = 150e3  # Resistance (in ohms)
C = 220e-12  # Capacitance (in farads)

# Calculate cutoff frequency (Hz)
fc = 1 / (2 * np.pi * R * C)

# Define frequency range (10 Hz to 100 kHz)
frequency_range = np.logspace(1, 5, 1000)

# Calculate magnitude of transfer function
H_magnitude = 1 / np.sqrt(1 + (frequency_range / fc)**2)

# Frequencies to mark
mark_freqs = [500, 1000, 2000, 4000, 5000, 6000, 10000]

# Plotting
plt.figure(figsize=(10, 6))
plt.semilogx(frequency_range, 20 * np.log10(H_magnitude), label='Frequency Response')
plt.axvline(fc, color='red', linestyle='--', label='Cutoff Frequency')
plt.axhline(-3, color='green', linestyle='--', label='-3 dB Point')

# Mark specific frequencies
for freq in mark_freqs:
    plt.scatter(freq, 20 * np.log10(1 / np.sqrt(1 + (freq / fc)**2)), color='blue', marker='o', label=f'{freq} Hz')

plt.annotate(f'Cutoff Frequency: {fc:.2f} Hz', xy=(fc, -5), xytext=(fc, -10), arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.title('Low-Pass Filter Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.legend()
plt.grid(True)
plt.savefig('1.png')
plt.show()

