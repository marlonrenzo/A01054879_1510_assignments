import doctest


def time_calculator(input_seconds):
    """
    Convert a number in seconds into days, hours, minutes and seconds.

    :precondition: input must be positive integer
    :postcondition: will return a formatted string that represents seconds as days, hours, minutes and seconds
    :param input_seconds: the numebr represented as seconds to be converted
    :return: the final conversion as a string
    """
    days = find_days(input_seconds)
    remainder_days = find_remainder(input_seconds, days, 86400)
    hours = find_hours(remainder_days)
    remainder_hours = find_remainder(remainder_days, hours, 3600)
    minutes = find_minutes(remainder_hours)
    remainder_minutes = find_remainder(remainder_hours, minutes, 60)
    seconds = remainder_minutes

    final_conversion = format_time(days, hours, minutes, seconds)
    return final_conversion


def find_remainder(original_value, converted_value, multiplier):
    """
    Determine the remainder of a number after it gets subracted by converted value in a number's place and multuplier.

    The converted value is multiplied by the multiplier that will equal the place value.

    :precondition: original value must be a positive integer
    :postcondition: will return a positive integer
    :param original_value: the value left for the next place value as an int
    :param converted_value: the value found in the place value as an int
    :param multiplier: the place value as an int
    :return: the excess value after subtracting the amount found in the place value as an int
    >>> find_remainder(1, 1, 0)
    1
    >>> find_remainder(100000, 5, 100)
    99500
    >>> find_remainder(785, 7, 5)
    750
    """
    excess_value = original_value - (converted_value * multiplier)
    return excess_value

def find_days(days_seconds):
    """
    Determine the number of days there are within the parameter.

    :precondition: the parameter must be a positive integer
    :postcondition: will return the number of days that were within the parameter
    :param days_seconds: an integer to convert into number of days
    :return: the number of days that were available within the parameter
    >>> find_days(86400)
    1
    >>> find_days(0)
    0
    >>> find_days(172800)
    2
    """
    if days_seconds >= 86400:
        days = int(days_seconds / 86400)
        return days
    elif days_seconds < 86400:
        return 0


def find_hours(hours_seconds):
    """
    Determine the number of hours there are within the parameter.

    :precondition: the parameter must be a positive integer
    :postcondition: will return the number of days that were within the parameter
    :param hours_seconds: an integer to convert into number of hours
    :return: the number of hours that were available within the parameter
    >>> find_hours(7200)
    2
    >>> find_hours(10)
    0
    >>> find_hours(3600)
    1
    """
    if hours_seconds >= 3600:
        hours = int(hours_seconds / 3600)
        return hours
    elif hours_seconds < 3600:
        return 0


def find_minutes(minute_seconds):
    """
    Determine the number of minutes there are within the parameter.

    :precondition: the parameter must be a positive integer
    :postcondition: will return the number of minutes that were within the parameter
    :param minute_seconds: an integer to convert into number of minutes
    :return: the number of minutes that were available within the parameter
    >>> find_minutes(120)
    2
    >>> find_minutes(59)
    0
    >>> find_minutes(60)
    1
    """
    if minute_seconds >= 60:
        minutes = int(minute_seconds / 60)
        return minutes
    elif minute_seconds < 60:
        return 0


def format_time(days_int, hours_int, minutes_int, seconds_int):
    """
    Format the parameters into a legible string.

    :precondition: parameters must be an integer equal to or more than zero
    :precondition: will return a concatenated string
    :return: the final conversion into a concatenated string
    >>> format_time(1, 2, 3, 4)
    '1days, 2hours, 3minutes, 4seconds'
    >>> format_time(0, 1, 0, 0)
    '0days, 1hours, 0minutes, 0seconds'
    >>> format_time("one","two","three","four")
    'onedays, twohours, threeminutes, fourseconds'
    """
    formatted_time = (str(days_int) + "days, " + str(hours_int) + "hours, " + str(minutes_int) + "minutes, " + str(seconds_int) + "seconds")

    return formatted_time

def main():
    """Run the program by calling the main function."""

    print(time_calculator(1382380))
    print(time_calculator(1))
    print(time_calculator(5678))
    doctest.testmod()


if __name__ == '__main__':
    main()


