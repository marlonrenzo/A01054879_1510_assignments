import doctest


def dijkstra(colours: list) -> list:
    """
    Sort the colours into a pattern resembling dutch flag.

    Capitalize all letters except for strings starting with 'b' in order to sort the way we need to.

    :param colours: a list
    :precondition: colours must be a non-empty list
    :post condition: will return a sorted list that resembles the dutch national flag
    :return: a list


    >>> dijkstra(['blue', 'white', 'blue', 'red', 'red', 'white'])
    ['red', 'red', 'white', 'white', 'blue', 'blue']
    >>> dijkstra(['blue', 'blue', 'blue', 'blue', 'red', 'white'])
    ['red', 'white', 'blue', 'blue', 'blue', 'blue']
    """
    for i in range(0, len(colours)):  # loop through the list and capitalize
        if colours[i][0] != 'b':
            colours[i] = colours[i].title()  # only capitalize strings that don't start with 'b'
    colours.sort()  # sort the colours by ascii value, so that capital letters are first, lowercase strings following
    for i in range(0, len(colours)):  # loop through the list of colours to lowercase the capitalized strings
        colours[i] = colours[i].lower()
    print(colours)


def main():
    """
    Call all functions to run the program.

    :return: None

    """
    doctest.testmod()
    dijkstra(['blue', 'white', 'blue', 'red', 'red', 'white'])


if __name__ == '__main__':
    main()
