import numpy as np
import matplotlib.pyplot as plt

# Define parameters
frequencies = [100, 200, 300]  # Frequencies in Hz
amplitudes = [1, 0.5, 0.3]      # Amplitudes
duration = 1                     # Duration in seconds
sampling_rate = 44100            # Sampling rate in Hz

# Generate time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate sine wave
signal = np.zeros_like(t)
for freq, amp in zip(frequencies, amplitudes):
    signal += amp * np.sin(2 * np.pi * freq * t)

# Plot the waveform
plt.plot(t, signal)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Generated Sine Wave')
plt.show()
