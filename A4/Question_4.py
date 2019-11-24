import doctest


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
    if not len(items):
        raise ValueError("Cannot enter an empty or non-sortable list")
    sorted_items = []
    while items:
        lowest_num = items[0]
        for number in items:
            if number < lowest_num:
                lowest_num = number
        items.remove(lowest_num)
        sorted_items.append(lowest_num)

    return sorted_items


def main():
    """
    Call all functions to run the program.

    :return: None

    """
    doctest.testmod()
    print(selection_sort([]))


if __name__ == '__main__':
    main()
