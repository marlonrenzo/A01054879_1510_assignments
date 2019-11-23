import doctest


def remove_multiples(set_of_nums: list, increment: int) -> list:
    """
    Remove all multiples of an increment.

    :param set_of_nums: a list
    :param increment: an int
    :precondition: set_of_nums must be a non-empty
    :precondition: increment must be a positive int
    :post condition: will return a new list without the multiples of the increment provided
    :return: a list

    >>> remove_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
    [1, 2, 3, 5, 7, 9]
    >>> remove_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3)
    [1, 2, 3, 4, 5, 7, 8, 10, 11]
    """
    new_numbers = []  # create a list that will be returned with an updated set of numbers
    for i in set_of_nums:  # loop thru the list of numbers
        if i % increment != 0 or i == increment:
            new_numbers.append(i)  # append the number if it's not the increment itself or it's not a multiple
    return new_numbers


def eratosthenes(upperbound: int) -> list:
    """
    Remove all non-prime numbers in a range between 2 and a upperbound.

    :param upperbound: an int
    :precondition: upperbound must be a positive int
    :post condition: will return an updated list of prime numbers between 2 and upperbound
    :return: return

    >>> eratosthenes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> eratosthenes(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    numbers = list(range(2, upperbound + 1))  # create a list between 0 and the upperbound
    counter = 0  # begin the counter at 2 as 1 and zero are not prime numbers
    while numbers[counter] < upperbound ** (1/2):  # loop thru numbers until it reaches the square root of upperbound
        numbers = remove_multiples(numbers, numbers[counter])  # update  numbers by removing multiples of current number
        counter += 1  # move on to the next number to check
    return numbers


def main():
    """
    Call all functions to run the program.

    :return: None

    """
    doctest.testmod()
    print(eratosthenes(100))


if __name__ == '__main__':
    main()
