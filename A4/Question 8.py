def find_largest(values, min_digit, max_digit):
    most_bars = 0
    for number in range(min_digit, max_digit):
        if values[number] > most_bars:
            most_bars = number
    return most_bars


def im_not_sleepy():
    digit_values = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    second = find_largest(digit_values, 0, 3)
    third = find_largest(digit_values, 0, 6)
    fourth = find_largest(digit_values, 0, 10)
    bars = 2 + digit_values[second] + digit_values[third] + digit_values[fourth]
    result = f"The time requiring the most amount of bars is:\n1{second}:{third}{fourth} with {bars} bars"
    return result


def main():
    print(im_not_sleepy())


if __name__ == '__main__':
    main()
