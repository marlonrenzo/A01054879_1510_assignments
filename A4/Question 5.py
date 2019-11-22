def breakdown_amount(cash: dict, amount: float):
    new_total = {}
    for money_value in cash.keys():
        if money_value < amount:
            new_total[money_value] = int(amount / money_value)
            amount -= money_value * new_total[money_value]
    return new_total


def cash_money(amount: float):
    if amount < 0:
        raise ValueError("The amount you entered is not a positive float number.")
    bills_and_coins = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
    return breakdown_amount(bills_and_coins, amount)


def main():
    print(cash_money(66.53))


if __name__ == '__main__':
    main()
