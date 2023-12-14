from typing import Callable

from Essentials.TailFibonacci.tail_recursion import tail_call_optimized


def fibonacci_impl() -> Callable[[int], int]:

    def fibonacci(x):
        @tail_call_optimized
        def fibonacci_tail(depth, step, current, previous):
            if depth == step:
                return current
            else:
                return fibonacci_tail(depth, step+1, previous+current, current)

        return x if x < 2 else fibonacci_tail(x, 2, 1, 1)

    return fibonacci
