import doctest


def breakdown_amount(cash: dict, amount: float) -> dict:
    """
    Calculate the amount each bill and coin is required to add to the amount.

    :param cash: a dict
    :param amount: a float
    :precondition: cash must be a properly formed dictionary
    :precondition: amount must be a positive float
    :post condition: will return an updated dictionary with values that sup up to the amount
    :return: a dict

    >>> money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
    >>> breakdown_amount(money, 66.53)
    {50: 1, 10: 1, 5: 1, 1: 1, 0.25: 2, 0.01: 3}
    """
    new_total = {}  # initiate a new list to return later with values
    for money_value in cash.keys():  # loop through the bills and coins in the dictionary
        if money_value <= amount:  # if the amount is greater than the current bill/coin, calculate number
            new_total[money_value] = int(amount / money_value)  # add the total and set the value to the quotient
            amount -= money_value * new_total[money_value]  # subtract the amount by the value of the bills/coins taken
    return new_total


def cash_money(amount: float) -> dict:
    """
    Determine the least number of bills and coins needed to make up an amount.

    :param amount: a float
    :precondition: amount must be a positive float
    :post condition: will return an updated dict containing the necessary bills to make up the amount
    :return: a dict

    >>> money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
    >>> breakdown_amount(money, 66.53)
    {50: 1, 10: 1, 5: 1, 1: 1, 0.25: 2, 0.01: 3}
    """
    if amount <= 0 or type(amount) != float:  # raise an error if the amount is less than zero
        raise ValueError("The amount you entered is not a positive float number.")
    bills_coins = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}  # bills/coins
    return breakdown_amount(bills_coins, amount)


def main():
    """
    Call all functions to run the program.

    :return: None

    """
    doctest.testmod()
    print(cash_money(4))


if __name__ == '__main__':
    main()
