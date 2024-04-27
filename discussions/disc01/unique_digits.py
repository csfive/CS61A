def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    unique = 0
    while n:
        last = n % 10
        n //= 10
        if not has_digit(n, last):
            unique += 1
    return unique


def unique_digits_alt(n):
    """Set comprehension

    >>> unique_digits_alt(8675309) # All are unique
    7
    >>> unique_digits_alt(13173131) # 1, 3, and 7
    3
    >>> unique_digits_alt(101) # 0 and 1
    2
    """
    return len({int(i) for i in str(n)})


def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    while n:
        last = n % 10
        n //= 10
        if last == k:
            return True
    return False


def has_digit_alt(n, k):
    assert k >= 0 and k < 10
    return str(k) in str(n)
