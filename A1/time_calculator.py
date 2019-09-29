import doctest


def time_calculator(input_seconds):
    """

    :param input_seconds:
    :return:
    """
    days = find_days(input_seconds)
    remainder_days = find_remainder(input_seconds, days, 86400)
    hours = find_hours(remainder_days)
    remainder_hours = find_remainder(remainder_days, hours, 3600)
    minutes = find_minutes(remainder_hours)
    remainder_minutes = find_remainder(remainder_hours, minutes, 60)
    seconds = remainder_minutes

    format_time(days, hours, minutes, seconds)


def find_remainder(original_value, converted_value, multiplier):
    """

    :param original_value:
    :param subtracting_value:
    :return:
    """
    excess_value = original_value - (converted_value * multiplier)
    return excess_value

def find_days(days_seconds):
    """

    :return:
    """
    if days_seconds > 86400:
        days = int(days_seconds / 86400)
        return days
    elif days_seconds < 86400:
        return 0


def find_hours(hours_seconds):
    """

    :return:
    """
    if hours_seconds > 3600:
        hours = int(hours_seconds / 3600)
        return hours
    elif hours_seconds < 3600:
        return 0


def find_minutes(minute_seconds):
    """

    :return:
    """
    if minute_seconds > 60:
        minutes = int(minute_seconds / 60)
        return minutes
    elif minute_seconds < 60:
        return 0


def format_time(days_int, hours_int, minutes_int, seconds_int):
    """

    :return:
    """
    formatted_time = (str(days_int) + "days, " + str(hours_int) + "hours, " + str(minutes_int) + "minutes, " + str(seconds_int) + "seconds")

    print(formatted_time)

def main():
    """

    :return:
    """

    print(time_calculator(1382380))
    print(time_calculator(1))
    print(time_calculator(5678))





if __name__ == '__main__':
    main()


