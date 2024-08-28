import numpy as np
import matplotlib.pyplot as plt

# Define the signal x[n]
n = np.arange(-10, 11)  # Discrete time indices
x = np.sinc(n)  # Example signal: sinc function

# Compute the DTFT of x[n]
omega = np.linspace(-np.pi, np.pi, 1000)
X = np.array([np.sum(x * np.exp(-1j * w * n)) for w in omega])

# Compute the autocorrelation of x[n]
R_x = np.correlate(x, x, mode='full')
m = np.arange(-len(x) + 1, len(x))

# Compute the DTFT of the autocorrelation sequence R_x[m]
R_x_dtft = np.array([np.sum(R_x * np.exp(-1j * w * m)) for w in omega])

# Verify the autocorrelation property
R_x_theoretical = np.abs(X) ** 2

# Plot the magnitude and phase of the DTFTs to compare
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(omega, np.abs(X), label='|X(e^{jω})|')
plt.title('Magnitude of X(e^{jω})')
plt.xlabel('ω')
plt.ylabel('Magnitude')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(omega, np.abs(R_x_dtft), label='|DTFT{R_x[m]}|', linestyle='--')
plt.plot(omega, R_x_theoretical, label='|X(e^{jω})|^2')
plt.title('Magnitude of Autocorrelation DTFT')
plt.xlabel('ω')
plt.ylabel('Magnitude')
plt.legend()
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(omega, np.angle(X), label='∠X(e^{jω})')
plt.title('Phase of X(e^{jω})')
plt.xlabel('ω')
plt.ylabel('Phase')
plt.grid()

plt.subplot(2, 2, 4)
plt.plot(omega, np.angle(R_x_dtft), label='∠DTFT{R_x[m]}', linestyle='--')
plt.plot(omega, np.angle(R_x_theoretical), label='∠|X(e^{jω})|^2')
plt.title('Phase of Autocorrelation DTFT')
plt.xlabel('ω')
plt.ylabel('Phase')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
