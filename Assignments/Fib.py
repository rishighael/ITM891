def fibonacci_series(n):
    """Generates the Fibonacci series up to the nth element."""
    if n < 0:
        print("Please enter a positive integer for n.")
        return

    elif n == 0:
        return []

    else:
        series = [0, 1]
        for i in range(2, n):
            next_term = series[i - 1] + series[i - 2]
            series.append(next_term)
        return series

# Get input from the user
nterms = int(input("Enter the number of terms: 10"))

# Call the function and print the result
print(fibonacci_series(nterms))