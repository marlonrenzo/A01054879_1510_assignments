import doctest

def compound_interest(principal, interest_rate, interest_per_year, years_to_grow):
    """
    Calculate total compound interest with given parameters.

    :precondition: all parameters must be positive integers
    :postcondition: will return a float with interest applied to it
    :param principal: the initial amount as an int
    :param interest_rate: rate at which interest is applied as an int
    :param interest_per_year: The number of compounding periods per year as an int
    :param years_to_grow: numbers of years to accumulate interest as an int
    :return: the final amount as a float
    """
    interest_rate = get_interest_rate(interest_rate)

    final_interest = get_final_interest(interest_rate, interest_per_year, years_to_grow)

    amount = principal * final_interest

    return amount


def get_final_interest(interest_rate, interest_per_year, years_to_grow):
    """
    Calculate the interest applied.

    :precondition: all parameters must be positive integers
    :postcondition: will return the interest to be applied as a float
    :param interest_rate: rate at which interest is applied as an int
    :param interest_per_year: The number of compounding periods per year as an int
    :param years_to_grow: numbers of years to accumulate interest as an int
    :return: the interest amount as a float
    >>> get_final_interest(5, 5, 10)
    1125899906842624.0
    >>> get_final_interest(1, 1, 1)
    2.0
    """
    interest_by_years = years_to_grow * interest_per_year
    rate_over_amount_per_year = (interest_rate / interest_per_year) + 1
    interest_amount = rate_over_amount_per_year ** interest_by_years

    return interest_amount


def get_interest_rate(rate):
    """
    Convert a percentage into a float.

    :precondition: must be a positive integer
    :postcondition: will return a percent as a decimal
    :param rate: an int
    :return: an interest rate as a float
    >>> get_interest_rate(2)
    0.02
    >>> get_interest_rate(123456789)
    1234567.89
    >>> get_interest_rate(999)
    9.99
    """
    rate = rate/100
    return rate


def main():
    """Run the program by calling the main function."""
    print(compound_interest(1000, 5, 12, 10))
    print(compound_interest(100, 2, 24, 40))
    print(compound_interest(456, 3, 4, 25))
    doctest.testmod()



if __name__ == '__main__':
    main()