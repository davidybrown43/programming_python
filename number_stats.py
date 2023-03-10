import math

# Prompt the user for a list of numbers
numbers = input("Enter a list of numbers separated by commas: ")

# Split the input string into a list of numbers
numbers_list = [float(num) for num in numbers.split(',')]

# Calculate the sum of the numbers
total = sum(numbers_list)

# Calculate the average of the numbers
average = total / len(numbers_list)

# Calculate the variance of the numbers
variance = sum((num - average) ** 2 for num in numbers_list) / len(numbers_list)

# Calculate the standard deviation of the numbers
std_dev = math.sqrt(variance)

# Output the statistics to the user
print(f"Sum: {total:.2f}")
print(f"Average: {average:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")
