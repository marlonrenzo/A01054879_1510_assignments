import doctest

def colour_mixer():
    input_one = input("Enter a primary colour here:\n")
    input_two = input("Enter a second primary colour here:\n")

    colour = add_colours(input_one, input_two)
    return colour


def add_colours(first_string, second_string):
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
    if string == "Purple" or string ==  "Green" or string ==  "Orange":
        return True
    else:
        return "Your entry is not valid, ensure you're adding different primary colours."


def format_input(string):
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




if __name__ == '__main__':
    main()