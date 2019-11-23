import doctest


def find_largest(values: dict, min_digit: int, max_digit: int) -> int:
    """
    Determine the number with the largest value within a dictionary between minimum and maximum digits.

    :param values: a dict
    :param min_digit: an int
    :param max_digit: an int
    :precondition: values must be a properly formatted dictionary with the correct values
    :precondition: min and max digits
    :post condition: will return the key in the dictionary with the highest value
    :return: an int

    >>> test = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    >>> find_largest(test, 0, 9)
    8

    """
    most_bars = 0  # set an arbitrary number
    for number in range(min_digit, max_digit):  # loop through the numbers between min_digit and max_digit
        if values[number] > most_bars:  # if loop is greater than the current larger # of bars, number is now largest
            most_bars = number
    return most_bars


def get_digits(digit_values) -> list:
    """
    Determine the bar value for each digit in a 12-hour clock.

    The first digit is not calculated as it is automatically 1 (to accomplish the most amount of bars).

    :return: a list

    >>> test = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    >>> get_digits(test)
    [1, 2, 5, 8]

    """
    first = 1  # first digit is skipped as it is automatically a 1
    second = find_largest(digit_values, 0, 3) # 2nd digit can only be 0, 1 or 2 (i.e. 10:00, 11:00 or 12:00)
    third = find_largest(digit_values, 0, 6)  # 3rd digit can only be 0 to 5 (i.e. 1:20, 1:00 or 1:50, but != 1:60)
    fourth = find_largest(digit_values, 0, 10) # 3rd digit can be 0 to 10 (i.e. 10:23, 11:07 or 12:59, etc.)
    return [first, second, third, fourth]


def get_time(digits: list) -> str:
    """
    Format a list of digits into a string that resembles a time from a 12-hour clock.

    :param digits: a list
    :precondition: must be a non-empty list of integers
    :post condition: will return a properly formatted time as a string
    :return: a str

    >>> test = [1, 2, 3, 4]
    >>> get_time(test)
    '12:34'

    >>> test = [1, 2, 3, 4]
    >>> get_time(test)
    '12:34'

    >>> test = [1, 2, 3, 4]
    >>> get_time(test)
    '12:34'

    """
    return f"{digits[0]}{digits[1]}:{digits[2]}{digits[3]}"


def get_bars(digits_values: dict, digits: list) -> int:
    """
    Get the total amount of bars of the digits provided.

    :param digits_values: a dict
    :param digits: a list
    :precondition: digit_values must be a dictionary with the correct values
    :precondition: digits must be a list with positive integers
    :post condition: will return the sum of the digits according to the value bound to it within digit_values
    :return: an int

    >>> test_dict = {1: 1, 2: 2, 3: 3, 4: 4}
    >>> test_digits = [1, 2, 3, 4]
    10

    >>> test_dict = {1: 1, 2: 2, 3: 3, 4: 4}
    >>> test_digits = [1, 1, 1, 1]
    4

    """
    bars = [digits_values[digits[0]], digits_values[digits[1]], digits_values[digits[2]], digits_values[digits[3]]]
    return sum(bars)  # sum of the list of values within digits_values that are bound to the items in digits


def im_not_sleepy() -> str:
    """
    Determine the time of a 12-hour alarm clock that requires the most amount of bars to display the numbers.

    Find the greatest amount for each digit, find the sum and print the time.

    :return: a str

    """
    digit_values = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}  # set values of digits with # of bars
    digits = get_digits(digit_values)  # get the digits of the time requiring the most bars
    bars = get_bars(digit_values, digits)  # sum of bars is all digits' corresponding value together
    time = get_time(digits)  # get the time with by giving get_time the digits found prior
    return f"The time requiring the most amount of bars is:\n{time} with {bars} bars"


def main():
    doctest.testmod()
    print(im_not_sleepy())


if __name__ == '__main__':
    main()
