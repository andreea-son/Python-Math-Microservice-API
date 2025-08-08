from utils.cache import cached_fib
from math import factorial, pow

class MathService:

    @staticmethod
    def compute_power(base: int, exponent: int) -> int:
        return int(pow(base, exponent))

    @staticmethod
    def compute_factorial(n: int) -> int:
        return factorial(n)

    @staticmethod
    def compute_fibonacci(n: int) -> int:
        return cached_fib(n)
