import numpy as np

# Linear Convolution using the convolution sum
def linear_convolution(x, h):
    N1 = len(x)
    N2 = len(h)
    N = N1 + N2 - 1  # Length of linear convolution
    y = np.zeros(N)
    for n in range(N):
        for k in range(N1):
            if n - k >= 0 and n - k < N2:
                y[n] += x[k] * h[n - k]
    return y

# Extract Circular Convolution from Linear Convolution
def circular_convolution_from_linear(linear_conv, N):
    return linear_conv[:N]

# Example sequences
x = [1, 2, 3, 4]
h = [1, 0, -1]

# Perform Linear Convolution
linear_conv = linear_convolution(x, h)

# Get Circular Convolution from Linear Convolution
circular_conv = circular_convolution_from_linear(linear_conv, max(len(x), len(h)))

# Print results
print("Linear Convolution:", linear_conv)
print("Circular Convolution:", circular_conv)

