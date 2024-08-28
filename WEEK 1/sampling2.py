import numpy as np
import matplotlib.pyplot as plt

# Define the sampling rate (fs) and signal frequency (f)
fs = 1000  # Hz
f = 100    # Hz

# Calculate the time vector
t = np.arange(0, 1, 1/fs)  # 1 second duration

# Generate the sinusoidal signal
x = np.sin(2 * np.pi * f * t)

# Plot the signal
plt.plot(t, x)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Sinusoidal Signal (1 kHz Sampling)")
plt.grid(True)
plt.show()
