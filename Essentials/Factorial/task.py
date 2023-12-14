from typing import Callable

from Essentials.Factorial.tail_recursion import tail_call_optimized


def factorial_impl() -> Callable[[int], int]:
    @tail_call_optimized
    def factorial(x):
        return 1 if x <= 1 else x*factorial(x-1)

    return factorial
