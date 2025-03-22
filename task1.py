from typing import Dict, Callable


def caching_fibonacci() -> Callable[[int], int]:
    # Create dict for memoization(caching)
    cache: Dict[int, int] = {}

    # Calculate fibonacci number using recursion and memoization(caching)
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# Example of use
fib = caching_fibonacci()
print(fib(10))
print(fib(15))
