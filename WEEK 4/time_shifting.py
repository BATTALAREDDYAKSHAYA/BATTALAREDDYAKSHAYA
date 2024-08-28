import numpy as np
import matplotlib.pyplot as plt

# Define the signal x[n]
n = np.arange(-10, 11)  # Discrete time indices
x = np.sinc(n)  # Example signal: sinc function

# Compute the DTFT of x[n]
omega = np.linspace(-np.pi, np.pi, 1000)
X = np.array([np.sum(x * np.exp(-1j * w * n)) for w in omega])

# Define the time-shifted signal x[n - n0]
n0 = 3  # Time shift
x_shifted = np.sinc(n - n0)

# Compute the DTFT of x[n - n0]
X_shifted = np.array([np.sum(x_shifted * np.exp(-1j * w * n)) for w in omega])

# Verify the time-shifting property
X_shifted_theoretical = np.exp(-1j * omega * n0) * X

# Plot the magnitude and phase of the DTFTs to compare
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(omega, np.abs(X), label='|X(e^{jω})|')
plt.title('Magnitude of X(e^{jω})')
plt.xlabel('ω')
plt.ylabel('Magnitude')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(omega, np.angle(X), label='∠X(e^{jω})')
plt.title('Phase of X(e^{jω})')
plt.xlabel('ω')
plt.ylabel('Phase')
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(omega, np.abs(X_shifted), label='|X_shifted(e^{jω})|', linestyle='--')
plt.plot(omega, np.abs(X_shifted_theoretical), label='|e^{-jωn0}X(e^{jω})|')
plt.title('Magnitude of Shifted X(e^{jω})')
plt.xlabel('ω')
plt.ylabel('Magnitude')
plt.legend()
plt.grid()

plt.subplot(2, 2, 4)
plt.plot(omega, np.angle(X_shifted), label='∠X_shifted(e^{jω})', linestyle='--')
plt.plot(omega, np.angle(X_shifted_theoretical), label='∠e^{-jωn0}X(e^{jω})')
plt.title('Phase of Shifted X(e^{jω})')
plt.xlabel('ω')
plt.ylabel('Phase')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

