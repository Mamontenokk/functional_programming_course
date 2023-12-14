from typing import Callable


class Integer:
    def __init__(self, value: int):
        self.value = value


def is_pure(increment_fn: Callable[[Integer], Integer]) -> bool:

    i = Integer(1)

    res1 = increment_fn(i)
    res2 = increment_fn(i)

    res3 = increment_fn(res2)

    if i.value == 1 and res1.value == 2 and res2.value == 2 and res3.value == 3:
        return True

    if i.value != 1:
        return False

    if res1.value != 2:
        return False

    if res1.value != res2.value:
        return False

    if res3.value != 2:
        return False

