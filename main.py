# Fibonacci Series

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        while len(fib_series) < n:
            next_num = fib_series[-1] + fib_series[-2]
            fib_series.append(next_num)
        return fib_series

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_numbers = fibonacci(n)
print(fib_numbers)
