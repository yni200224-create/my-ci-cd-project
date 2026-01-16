import string

def my_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def my_start_str() -> str:
    return "Hello world!"
