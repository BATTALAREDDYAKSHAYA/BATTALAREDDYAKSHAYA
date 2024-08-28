def circular_shift(x,m):
    n = len(x)
    # Ensure the shift is within the length of the list
    m = m % n
    
    # Perform the circular shift
    return x[-m:] + x[:-m]

# Test the function
example_list = [1, 2, 3, 4, 5]

# Circular shift to the right by 2 positions
print(circular_shift(example_list, 2))  # Output: [4, 5, 1, 2, 3]

# Circular shift to the left by 2 positions
print(circular_shift(example_list, -2))  # Output: [3, 4, 5, 1, 2]


def circular_shift(lst, shift):
    n = len(lst)
    # Ensure the shift is within the length of the list
    shift = shift % n
    
    # Perform the circular shift
    return lst[-shift:] + lst[:-shift]

# Take input from the user for the list
user_input = input("Enter the list of numbers separated by spaces: ")
# Convert the user input string to a list of integers
example_list = list(map(int, user_input.split()))

# Take input from the user for the number of positions to shift
shift_amount = int(input("Enter the number of positions to shift: "))

# Call the circular shift function and print the result
shifted_list = circular_shift(example_list, shift_amount)
print("The shifted list is:", shifted_list)

