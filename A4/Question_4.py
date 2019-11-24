import doctest


def find_lowest_value(items: list) -> int:
    """
    Determine the lowest value in a list of items.

    :param items: a list
    :return: an int

    >>> test = [1, 10, 10, 10]
    >>> find_lowest_value(test)
    1

    >>> test = [1000, 1001]
    >>> find_lowest_value(test)
    1000

    """
    lowest_num = items[0]  # an arbitrary number to create an initial lowest number
    for number in items:  # loop through the numbers
        if number < lowest_num:  # if the number is lower than current value of lowest_num, number is the new low num
            lowest_num = number
    return lowest_num


def selection_sort(items: list) -> list:
    """
    Sort items in a list without the use of builtin functions.

    Return a new sorted list items.

    :param items: a list
    :return: a list

    >>> selection_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> selection_sort([15, 14, 13, 12, 11])
    [11, 12, 13, 14, 15]
    """
    try:
        sorted(items)  # try an action that will raise a TypeError if items is a non-sortable list
        items[0] = items[0]  # try an action that will raise an IndexError if items is an empty list
    except TypeError or IndexError:  # except the two errors if they are raised by the above statements
        raise ValueError("The input should be a non-empty sortable list.")
    else:  # run the code as normal
        sorted_items = []  # initiate a new list that will have the sorted items
        while items:  # loop while items has elements in it
            lowest_value = find_lowest_value(items)  # find the lowest number currently
            items.remove(lowest_value)  # remove the lowest number from the original list
            sorted_items.append(lowest_value)  # append the lowest number to the new list
        return sorted_items


def main():
    """
    Call all functions to run the program.

    :return: None

    """
    doctest.testmod()
    print(selection_sort(['yo', 'yooo', 'y', 'yoo']))


if __name__ == '__main__':
    main()
