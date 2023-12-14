from typing import Callable


def fibonacci_impl() -> Callable[[int], int]:
    def fibonacci(x):
        return x if x <= 1 else fibonacci(x-1) + fibonacci(x-2)

    return fibonacci
