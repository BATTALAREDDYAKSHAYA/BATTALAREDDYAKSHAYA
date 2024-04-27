import csv
# Data to be written to the CSV file
data = [
    ['Name', 'Age', 'Gender'],
    ['John', 25, 'Male'],
    ['Lisa', 30, 'Female'],
    ['Bob', 35, 'Male']
]
# Open a CSV file in write mode
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

#Reading from a CSV File:
# Open a CSV file in read mode
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Writing to a Numpy Binary File:
import numpy as np

# Data to be written to the Numpy binary file
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Save data to a Numpy binary file
np.save('data.npy', data)

#Reading from a Numpy Binary File:
# Load data from a Numpy binary file
loaded_data = np.load('data.npy')

print(loaded_data)

#Pickle:
#Writing to a Pickle File:
import pickle

# Data to be written to the Pickle file
data = {'Name': 'John', 'Age': 30, 'Gender': 'Male'}

# Open a Pickle file in write mode
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

#Reading from a Pickle File:
# Open a Pickle file in read mode
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
