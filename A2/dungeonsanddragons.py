import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """
    Will return a random positive integer base on the parameters.

    :precondition: both parameters must be positive.
    :post condition: will return a sum of x amount of rolls on a y-sided die
    :param number_of_rolls: an integer determining how many times to roll the die
    :param number_of_sides: an integer determining the upper bound of one roll
    :return: a random integer containing the sum of all rolls performed
    """
    total = 0
    if number_of_rolls <= 0 or number_of_sides <= 0:
        return 0
    else:
        for x in range(0, number_of_rolls):
            roll = random.randint(1, number_of_sides)
            total = total + roll
        return total


def choose_inventory(inventory, selection):
    """
    Select items from inventory and place into a sorted list.

    Check all cases ranging from empty lists, 0 selections or negative selections and print a warning for these cases.

    :precondition: selection must be a positive integer less than or equal to the length of inventory
    :precondition: inventory must not be an empty list
    :post condition: a sorted list with selected items, the length of the list depends on the value of selections
    :param inventory: a list with items to select from
    :param selection: an integer for the number of selections from the list
    :return: a sorted list
    >>> choose_inventory([],0)
    []
    >>> choose_inventory(['One'],-1)
    Warning: Your selection of items for inventory items is a negative number.
    []
    >>> choose_inventory(['first','second','third'],4)
    Warning: Your Selection of items for inventory items is a larger than the amount items available.
    ['first', 'second', 'third']
    """
    if inventory == [] and selection == 0:
        return []
    elif selection < 0:
        print("Warning: Your selection of items for inventory items is a negative number.")
        return []
    elif selection > (len(inventory)):
        print("Warning: Your Selection of items for inventory items is a larger than the amount items available.")
        sorted_inventory = sorted(inventory)
        return sorted_inventory
    else:
        random_selection = random.sample(inventory, selection)
        random_selection.sort()
        return random_selection


def create_character(name_length):
    """
    Create a list including items to associate to a character.

    Each list element, except for the character name, will be a mini list containing an attribute along with a value.
    :precondition: parameter must be a positive integer
    :post condition: will create a character as a list of attributes
    :param name_length: an integer
    :return:
    """
    character = {'Name': generate_name(name_length // 2), 'Strength': roll_die(3, 6),
                 'Dexterity': roll_die(3, 6), 'Constitution': roll_die(3, 6),
                 'Intelligence': roll_die(3, 6), 'Wisdom': roll_die(3, 6),
                 'Charisma': roll_die(3, 6)}
    return character


def print_character(character):
    """
    Format character's attributes in a neat and legible way.

    Check the length of the list provided, and ensure it it formatted properly.

    Include the inventory items associated with the character when the length of the list is 8.
    :precondition: the character list must be properly formatted
    :post condition: will print all the attributes in a legible way
    :param character: a list with all character attributes
    :return: formatted string with all character attributes
    >>> print_character(['Hi', ['one', 12], ['two', 9], ['three', 10], ['four', 12], ['five', 13], ['six', 13]])
    Name: Hi
    one: 12
    two: 9
    three: 10
    four: 12
    five: 13
    six: 13
    >>> print_character(['.', ['one', -49], ['two', 0], ['three', 5000], ['four', 1], ['five', 17], ['six', 'seven']])
    Name: .
    one: -49
    two: 0
    three: 5000
    four: 1
    five: 17
    six: seven
    """
    if len(character) == 7:
        print(f"Name: {character[0]}")
        print(f"{character[1][0]}: {character[1][1]}")
        print(f"{character[2][0]}: {character[2][1]}")
        print(f"{character[3][0]}: {character[3][1]}")
        print(f"{character[4][0]}: {character[4][1]}")
        print(f"{character[5][0]}: {character[5][1]}")
        print(f"{character[6][0]}: {character[6][1]}")
    elif len(character) == 8:
        print(f"Name: {character[0]}")
        print(f"{character[1][0]}: {character[1][1]}")
        print(f"{character[2][0]}: {character[2][1]}")
        print(f"{character[3][0]}: {character[3][1]}")
        print(f"{character[4][0]}: {character[4][1]}")
        print(f"{character[5][0]}: {character[5][1]}")
        print(f"{character[6][0]}: {character[6][1]}")
        print("--Here are your inventory items--")
        for length in range(0, len(character[7])):
            print(character[7][length])
    else:
        print("Warning: Error found with your list of character attributes")


def select_race():
    pass


def generate_character():
    pass

if __name__ == '__main__':
    doctest.testmod()