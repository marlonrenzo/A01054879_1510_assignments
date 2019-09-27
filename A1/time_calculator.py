def time_calculator(input_seconds):
    """

    :param input_seconds:
    :return:
    """
    days = find_days(input_seconds)
    remainder = find_remainder(input_seconds, days)
    hours = find_hours(remainder)
    remainder = find_remainder(remainder, hours)
    minutes = find_minutes(remainder)
    remiander = find_remainder(remainder, minutes)
    seconds = remainder
    print(format_time(days, hours, minutes, seconds))



def find_days(seconds):
    """

    :return:
    """
    if seconds > 86400:
        days = seconds / 86400 - seconds % 86400
        return days
    elif seconds < 86400:
        return seconds


def find_hours(seconds):
    """

    :return:
    """
    if seconds > 3600:
        hours = seconds / 3600 - seconds % 3600
        return days
    elif seconds < 3600:
        return seconds


def find_minutes(seconds):
    """

    :return:
    """
    if seconds > 60:
        hours = seconds / 60 - seconds % 60
        return days
    elif seconds < 60:
        return seconds


def format_time(days, hours, minutes, seconds):
    """

    :return:
    """
    formatted_time = (days + "" + hours + "" + minutes + "" + seconds)

    return formatted_time

def main():
    """

    :return:
    """
    time_calculator(172810)



if __name__ == 'main':
    main()


