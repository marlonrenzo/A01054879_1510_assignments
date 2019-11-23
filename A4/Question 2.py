import doctest


def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor of two integers.


    Use recursion to continue dividing the numbers until a remainder of zero is found, then return the lower of the two
    numbers to get the GCD.

    :param a: an int
    :param b: an int
    :precondition: a and b must be integers
    :post condition: will return the greatest common divisor of the two integers
    :return: an int

    >>> gcd(270, 192)
    6
    >>> gcd(5, 25)
    5
    >>> gcd(100, 50)
    255
    """
    remainder = max(abs(a), abs(b)) % min(abs(a), abs(b))  # get remainder of high num divided by low num, ignore negative signs with abs()
    if remainder > 0:
        return gcd(remainder, min(abs(a), abs(b)))  # run the function again with the remainder and the lower num
    return min(abs(a), abs(b))  # return the lower number if the remainder is zero to get the greatest common divisor


def main():
    """
    Call all functions to run the program.

    :return: None

    """
    doctest.testmod()
    print(gcd(270, 192))


if __name__ == '__main__':
    main()
