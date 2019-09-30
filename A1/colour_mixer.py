import doctest

def colour_mixer():
    """
    Add two user-inputted primary colours to a secondary colour.

    :return: a string
    """
    input_one = input("Enter a primary colour here:\n")
    input_two = input("Enter a second primary colour here:\n")

    colour = add_colours(input_one, input_two)
    return colour


def add_colours(first_string, second_string):
    """
    Add the two colours together to get a secondary colour.

    :precondition: parameters must be two different primary colours
    :postcondition: will return a secondary colour
    :param first_string: user input as a string
    :param second_string: second user input as a string
    :return: a string
    >>> add_colours("BLUE", "reD")
    'Purple'
    >>> add_colours("YELLOW", "blue")
    'Green'
    >>> add_colours("blue", "blue")
    "Your entry is not valid, ensure you're adding different primary colours."
    """
    first_string = format_input(first_string)
    second_string = format_input(second_string)

    string = first_string + second_string

    colour = colour_replace(string)
    valid_colour = check_colour(colour)
    if valid_colour == True:
        return colour
    else:
        return valid_colour


def check_colour(string):
    """
    Check to see if the string is a valid input.

    :precondition: must be a string
    :postcondition: will return the validity
    :param string: a string to be checked
    :return: will determine the validity of the string
    >>> check_colour("Purple")
    True
    >>> check_colour("redred")
    "Your entry is not valid, ensure you're adding different primary colours."
    >>> check_colour("blueered")
    "Your entry is not valid, ensure you're adding different primary colours."
    >>> check_colour("Green")
    True
    """
    if string == "Purple" or string ==  "Green" or string ==  "Orange":
        return True
    else:
        return "Your entry is not valid, ensure you're adding different primary colours."


def format_input(string):
    """
    Format a string to match the same look.

    :precondition: parameter must be a string
    :postcondition: will return a formatted string
    :param string: the string to be formatted
    :return: a stripped and lowercased string
    >>> format_input("  ASdfGhJkl  ")
    'asdfghjkl'
    >>> format_input("QWERTY")
    'qwerty'
    >>> format_input("      BlUe")
    'blue'
    """
    string = string.lower()
    string = string.strip()

    return string


def colour_replace(combination):
    """
    Replace the added colours into a secondary colour.

    :precondition: combination must be a string matching one of the following listen below
    :postcondition: will return a secodnary colour as a string
    :param combination: the added colours as a string
    :return: a string
    >>> colour_replace("bluered")
    'Purple'
    >>> colour_replace("yellowwwwreddddd")
    'yellowwwwreddddd'
    >>> colour_replace("redyellow")
    'Orange'
    """
    combination = combination.replace("bluered", "Purple")
    combination = combination.replace("redblue", "Purple")
    combination = combination.replace("yellowblue", "Green")
    combination = combination.replace("blueyellow", "Green")
    combination = combination.replace("redyellow", "Orange")
    combination = combination.replace("yellowred", "Orange")

    return combination




def main():
    """Run the program by calling the main function."""
    print(colour_mixer())
    doctest.testmod()




if __name__ == '__main__':
    main()