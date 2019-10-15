import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """
    Return a random positive integer base on the parameters.

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
    print("Welcome to the Olde Tyme Merchant!\n\nHere is what we have for sale:\n")
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


def create_character():
    """
    Create a dictionary including attributes to associate to a character.

    :post condition: will create a character as a dictionary of attributes
    :return: the information of a character as a dictionary
    """
    char_class = select_class()
    hp = roll_hp(char_class)
    character = {'Name': get_character_name(), 'Race': select_race(), 'Class': char_class, 'HP': [hp, hp],
                 'Strength': roll_die(3, 6), 'Dexterity': roll_die(3, 6), 'Constitution': roll_die(3, 6),
                 'Intelligence': roll_die(3, 6), 'Wisdom': roll_die(3, 6), 'Charisma': roll_die(3, 6), 'XP': 0}
    return character


def roll_hp(character_class):
    if character_class == 'barbarian':
        return roll_die(1, 12)
    elif character_class == 'bard' or 'cleric' or 'druid' or 'monk' or 'rogue' or 'warlock':
        return roll_die(1, 8)
    elif character_class == 'fighter' or 'paladin' or 'ranger':
        return roll_die(1, 10)
    elif character_class == 'sorcerer' or 'wizard':
        return roll_die(1, 6)
    else:
        return 'Error'


def get_character_name():
    """
    Ask the user for a name for their new character.
    :return: the user's input as a string
    """
    user_name = input("Enter your character's name:\n")
    return user_name.strip().capitalize()


def print_character(character):
    """
    Format character's attributes in a neat and legible way.

    Check the length of the list provided, and ensure it is formatted properly.

    Include the inventory items associated with the character when the length of the list is 8.
    :precondition: the character list must be properly formatted
    :post condition: will print all the attributes in a legible way
    :param character: a list with all character attributes
    :return: formatted string with all character attributes
    >>> print_character({'Name': 'Hi', 'a': 'dwarf', 'b': 'cleric', 'c': [7, 7], 'd': 7, 'e': 11, 'f': 10, 'g': 10, 'h': 16, 'i': 8, 'j': 0})
    Name: Hi
    a: dwarf
    b: cleric
    c: 7/7
    d: 7
    e: 11
    f: 10
    g: 10
    h: 16
    i: 8
    j: 0
    >>> print_character({'Name': 'Hi', 'a': 'dwarf', 'b': 'cleric', 'c': [7, 7], 'd': 7, 'e': 11, 'f': 10, 'g': 10, 'h': 16, 'i': 8, 'j': 0})
    Name: Hi
    a: dwarf
    b: cleric
    c: 7/7
    d: 7
    e: 11
    f: 10
    g: 10
    h: 16
    i: 8
    j: 0
    """
    if len(character) == 11:
        print(f"Name: {character['Name']}")
        print(f"Race: {character['Race']}")
        print(f"Class: {character['Class']}")
        print(f"HP: {character['HP'][1]}/{character['HP'][0]}")
        print(f"Strength: {character['Strength']}")
        print(f"Dexterity: {character['Dexterity']}")
        print(f"Constitution: {character['Constitution']}")
        print(f"Intelligence: {character['Intelligence']}")
        print(f"Wisdom: {character['Wisdom']}")
        print(f"Charisma: {character['Charisma']}")
        print(f"Experience: {character['XP']}")
    # elif len(character) == 12:
    #     print(f"Name: {character[0]}")
    #     print(f"{character[1][0]}: {character[1][1]}")
    #     print(f"{character[2][0]}: {character[2][1]}")
    #     print(f"{character[3][0]}: {character[3][1]}")
    #     print(f"{character[4][0]}: {character[4][1]}")
    #     print(f"{character[5][0]}: {character[5][1]}")
    #     print(f"{character[6][0]}: {character[6][1]}")
    #     print("--Here are your inventory items--")
    #     for length in range(0, len(character[7])):
    #         print(character[7][length])

    else:
        print("Warning: Error found with your list of character attributes")


def select_race():
    """
    Ask the user to select a race from a list of varied races provided in a dictionary.

    Print out the races in a neatly-formatted manner using a for loop and f-strings.

    User must enter a number that is included in the list of available selections.
    :return: the user-selected race
    """
    race = {1: "Dwarf", 2: "Elf", 3: "Gnome", 4: "Dwarf", 5: "Human", 6: "Dragonborn", 7: "Halfling", 8: "Half-Orc", 9: "Half-Elf", 10: "Tiefling"}
    for x in range(1, 11):
        print(f"{x}. {race[x]}")

    user_race = int(input("Select your race (by number):\n"))
    race = race[user_race].lower()
    return race


def select_class():
    """
    Ask the user to select a class from a list of varied classes provided in a dictionary.

    Print out the classes in a neatly-formatted manner using a for loop and f-strings.

    User must enter a number that is included in the list of available selections.
    :return: the user-selected class
    """
    classes = {1: "Barbarian", 2: "Bard", 3: "Cleric", 4: "Druid",
               5: "Fighter", 6: "Monk", 7: "Paladin", 8: "Ranger",
               9: "Rogue", 10: "Sorcerer", 11: "Warlock", 12: "Wizard"}
    for x in range(1, 13):
        print(f"{x}. {classes[x]}")

    user_class = int(input("Select your class (by number):\n"))
    selected_class = classes[user_class].lower()
    return selected_class


def combat_round():
    pass


if __name__ == '__main__':
    # doctest.testmod()
    # print(select_race())
    new_character = create_character()
    print(new_character)
    print_character(new_character)
