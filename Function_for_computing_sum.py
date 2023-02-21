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