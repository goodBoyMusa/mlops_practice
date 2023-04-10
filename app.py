import numpy as np

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Convert the list to a numpy array
arr = np.array(numbers)

# Use numpy to calculate the sum, mean, and standard deviation of the array
total = np.sum(arr)
average = np.mean(arr)
std_dev = np.std(arr)

# Print the results to the console
print("The sum of the numbers is:", total)
print("The average of the numbers is:", average)