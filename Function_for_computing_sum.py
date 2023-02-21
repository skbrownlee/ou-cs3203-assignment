def sum(arr):
    """
    Compute the sum of an array of numbers.
    """
    total = 0
    for num in arr:
        total += num
    return total

def product(arr):
    """
    Compute the product of an array of numbers.
    """
    product = 1
    for num in arr:
        product *= num
    return product

def reverse(arr):
    """
    Reverse an array of numbers using list slice notation
    """
    return arr[::-1]

# Prompt user to enter a list of numbers separated by spaces
input_string = input("enter a list of numbers separated by spaces: ")

# Split the input string  into an array of strings with space as the delimiter
num_strings = input_string.split()

# Convert the array of strings into an array of integers
num_array = [int(num_string) for num_string in num_strings]

# Print the sum of the numbers
print("Sum: ", sum(num_array))

# Print the product of the numbers
print("Product: ", product(num_array))