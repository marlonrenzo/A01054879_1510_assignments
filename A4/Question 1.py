import doctest


def remove_multiples(set_of_nums, increment):
    new_numbers = []  # create a list that will be returned with an updated set of numbers
    for i in set_of_nums:  # loop thru the list of numbers
        if i % increment != 0 or i == increment:
            new_numbers.append(i)  # append the number if it's not the increment itself or it's not a multiple
        elif i % increment == 0:  # if the number is a multiple, don't append it to the updated list
            continue
    return new_numbers


def eratosthenes(upperbound):
    numbers = list(range(2, upperbound + 1))  # create a list between 0 and the upperbound
    counter = 0  # begin the counter at 2 as 1 and zero are not prime numbers
    while numbers[counter] < upperbound ** (1/2):  # loop thru numbers until it reaches the square root of upperbound
        numbers = remove_multiples(numbers, numbers[counter])  # update  numbers by removing multiples of current number
        counter += 1  # move on to the next number to check

    return numbers


def main():
    doctest.testmod()
    print(eratosthenes(100))


if __name__ == '__main__':
    main()
