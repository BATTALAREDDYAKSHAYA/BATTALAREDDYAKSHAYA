import soundfile as sf
import matplotlib.pyplot as plt

# Load audio file
file_path = '/home/rguktrkvalley/Downloads/Chorus.wav'
signal, sample_rate = sf.read(file_path)

# Calculate time array
duration = len(signal) / sample_rate
time = [i / sample_rate for i in range(len(signal))]

# Plot the signal
plt.figure(figsize=(10, 4))
plt.plot(time, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Audio Signal')
plt.grid(True)
plt.show()

