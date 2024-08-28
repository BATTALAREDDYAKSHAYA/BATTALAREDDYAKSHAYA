import numpy as np
import matplotlib.pyplot as plt

# Define parameters
f = 200                # Frequency in Hz
T = 0.5                # Duration in seconds
fs = 8000              # Sampling rate in Hz
A = 1                  # Amplitude

# Create time vector
t = np.arange(0, T, 1/fs)

# Generate sinusoidal signal
y = A * np.sin(2 * np.pi * f * t)

# Plot the signal
plt.figure(figsize=(10, 4))
plt.plot(t, y)
plt.title("200 Hz Sinusoidal Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
