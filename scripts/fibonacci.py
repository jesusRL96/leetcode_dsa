import sys


def fibonacci(n: int):
    if n <= 1:
        return n
    fibonacci_n1 = fibonacci(n - 1)
    fibonacci_n2 = fibonacci(n - 2)
    fibonacci_n = fibonacci_n1 + fibonacci_n2
    return fibonacci_n


if __name__ == "__main__":
    n = sys.argv[1]
    f_r = fibonacci(int(n))
    print(f_r)
