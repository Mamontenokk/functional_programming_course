def is_prime(n: int) -> bool:

    def is_prime_helper(n: int, i: int):
        if n <= 1:
            return False

        if n == i:
            return True

        if n % i == 0:
            return False

        if i > pow(n, 0.5):
            return True

        return is_prime_helper(n, i+1)

    return is_prime_helper(n, 2)




