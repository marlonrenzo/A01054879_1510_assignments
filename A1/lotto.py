import random

def number_generator():
    """
    Generate a set of 6 random unique numbers ranging from 1 to 49.

    :return: a sorted list of unique random numbers
    """
    numbers = random.sample(range(1, 49), 6)
    numbers.sort()
    return numbers


def main():
    """Run the program by calling the main function."""
    print(number_generator())




if __name__ == '__main__':
    main()
