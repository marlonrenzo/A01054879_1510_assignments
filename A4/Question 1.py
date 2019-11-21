def remove_multiples(set_of_nums, multiple):
    new_numbers = []
    for i in set_of_nums:
        if i % multiple != 0 or i == multiple:
            new_numbers.append(i)
        elif i % multiple == 0:
            continue
    return new_numbers


def remove_zero_and_one(set_of_nums):
    new_numbers = []
    for i in set_of_nums:
        if i != 0 and i != 1:
            new_numbers.append(i)
    return new_numbers


def eratosthenes(upperbound):
    numbers = list(range(0, upperbound + 1))
    counter = 2
    numbers = remove_zero_and_one(numbers)
    while counter < upperbound ** (1/2):
        numbers = remove_multiples(numbers, counter)
        counter += 1

    return numbers


def main():
    print(eratosthenes(100))


if __name__ == '__main__':
    main()
