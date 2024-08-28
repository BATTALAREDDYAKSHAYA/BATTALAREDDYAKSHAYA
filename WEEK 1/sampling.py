import numpy as np
import matplotlib.pyplot as plt

# Step 1: Take an array input from the user
user_input = input("Enter an array of numbers separated by spaces: ")
array = np.array([float(num) for num in user_input.split()])

# Step 2: Display the original array
print("Original array:", array)

# Step 3: Perform up-sampling (e.g., repeating each element twice)
up_sampling_factor = 2
up_sampled_array = np.repeat(array, up_sampling_factor)
print("Up-sampled array:", up_sampled_array)

# Step 4: Perform down-sampling (e.g., selecting every second element)
down_sampling_factor = 2
down_sampled_array = array[::down_sampling_factor]
print("Down-sampled array:", down_sampled_array)

# Step 5: Plot the original, up-sampled, and down-sampled arrays
plt.figure(figsize=(12, 6))

# Original array plot
plt.subplot(3, 1, 1)
plt.plot(array, marker='o')
plt.title('Original Array')
plt.grid(True)

# Up-sampled array plot
plt.subplot(3, 1, 2)
plt.plot(up_sampled_array, marker='o')
plt.title('Up-sampled Array')
plt.grid(True)

# Down-sampled array plot
plt.subplot(3, 1, 3)
plt.plot(down_sampled_array, marker='o')
plt.title('Down-sampled Array')
plt.grid(True)

plt.tight_layout()
plt.show()
