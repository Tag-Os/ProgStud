import math

def count_divisors(n):
    """
    Возвращает количество натуральных делителей числа n.

    >>> count_divisors(1)
    1
    >>> count_divisors(2)
    2
    >>> count_divisors(4)
    3
    >>> count_divisors(12)
    6
    >>> count_divisors(16)
    5
    >>> count_divisors(17)
    2
    >>> count_divisors(36)
    9

    Проверка для простых чисел:
    >>> count_divisors(13)
    2
    >>> count_divisors(19)
    2

    Проверка для квадратов простых чисел:
    >>> count_divisors(9)
    3
    >>> count_divisors(25)
    3

    Проверка типа возвращаемого значения:
    >>> isinstance(count_divisors(100), int)
    True
    """
    count = 0
    limit = math.isqrt(n)
    for i in range(1, limit + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)