import doctest


def find_largest(values: dict, min_digit: int, max_digit: int) -> int:
    """
    Determine the number with the largest value within a dictionary between minimun and maximun digits.

    :param values: a dict
    :param min_digit: an int
    :param max_digit: an int
    :precondition: values must be a properly formatted dictionary with the correct values
    :precondition: min and max digits
    :post condition: will return the key in the dictionary with the highest value
    :return: an int

    >>>find_largest()
    """
    most_bars = 0
    for number in range(min_digit, max_digit):
        if values[number] > most_bars:
            most_bars = number
    return most_bars


def im_not_sleepy() -> str:
    """
    Determine the time that requires the most amount of bars to display a given time.

    Find the greatest amount for each digit, find the sum and print the time.

    :return: a str

    """
    digit_values = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    second = find_largest(digit_values, 0, 3)
    third = find_largest(digit_values, 0, 6)
    fourth = find_largest(digit_values, 0, 10)
    bars = 2 + digit_values[second] + digit_values[third] + digit_values[fourth]
    return f"The time requiring the most amount of bars is:\n1{second}:{third}{fourth} with {bars} bars"


def main():
    doctest.testmod()
    print(im_not_sleepy())


if __name__ == '__main__':
    main()
