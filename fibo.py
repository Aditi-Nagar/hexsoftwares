def generate_fibonacci(n):
    """
    Generate a list of the first `n` Fibonacci numbers using an iterative approach.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        List[int]: A list containing the first `n` Fibonacci numbers.
    """
    if n <= 0:
        raise ValueError("The number of Fibonacci numbers to generate must be a positive integer.")
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci_series = [0, 1]
    
    while len(fibonacci_series) < n:
        next_value = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_value)
    
    return fibonacci_series

# Example usage
try:
    num = int(input("Enter the number of Fibonacci numbers to generate: "))
    if num < 0:
        raise ValueError("The number of Fibonacci numbers must be a non-negative integer.")
    print(generate_fibonacci(num))
except ValueError as e:
    print(f"Error: {e}")
