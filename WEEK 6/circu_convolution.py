import numpy as np

def circular_convolution_direct(x, h):
    # Ensure both sequences are the same length by padding the shorter one
    N = max(len(x), len(h))
    x = np.pad(x, (0, N - len(x)), mode='constant')
    h = np.pad(h, (0, N - len(h)), mode='constant')

    # Initialize the result array
    result = np.zeros(N)

    # Perform the circular convolution
    for n in range(N):
        for m in range(N):
            result[n] += x[m] * h[(n - m) % N]

    return result

# Example usage:
x = np.array([1, 2, 3, 4])   # First input sequence
h = np.array([-1,0,5,3])  # Second input sequence

# Perform circular convolution
output_direct = circular_convolution_direct(x, h)
print("Circular Convolution Result (Direct):", output_direct)

