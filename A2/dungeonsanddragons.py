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


def choose_inventory():
    """
    Select items from inventory and place into a list.

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
    shop_items = {1: 'sword', 2: 'dagger', 3: 'battleaxe', 4: 'spear', 5: 'quarterstaff', 6: 'shield', 7: 'potion '}
    items = []
    print("\n -----Welcome to the Olde Tyme Merchant!-----\n\nHere is what we have for sale:\n")
    for x in range(1, 8):
        print(f"{x}. {shop_items[x]}")
    item_selection = int(input("Enter the number of the item you would like to buy (-1 to finish shopping)\n"))
    if 7 >= item_selection > 0:

        item = shop_items[item_selection]
        del shop_items[item_selection]
        items.append(item)
        shop_items[item_selection] = 'Sold'
    elif item_selection == -1:
        print("Thank you for shopping, here are your items.")
        return items
    elif len(shop_items) == 0:
        print("There are no more items to select.")
        item_selection = -1
    else:
        print("Invalid entry. Please select from the available items (by number).\n")

    while item_selection >= 0 and len(shop_items) > 0:
        for x in range(1, 8):
            print(f"{x}. {shop_items[x]}")
        item_selection = int(input("Enter the number of the item you would like to buy (-1 to finish shopping)\n"))
        if 7 >= item_selection > 0:
            shop_items_sold = shop_items
            item = shop_items[item_selection]
            del shop_items[item_selection]
            items.append(item)
            shop_items_sold[item_selection] = 'Sold'
        elif item_selection == -1:
            print("Thank you for shopping, here are your items.")
            return items
        elif len(shop_items) == 0:
            print("There are no more items to select.")
            item_selection = -1
        else:
            print("Invalid entry. Please select from the available items (by number).\n")



def create_character():
    """
    Create a dictionary including attributes to associate to a character.

    :post condition: will create a character as a dictionary of attributes
    :return: the information of a character as a dictionary
    """
    char_class = select_class()
    hp = roll_hp(char_class)
    character = {'Name': get_character_name(4), 'Race': select_race(), 'Class': char_class, 'HP': [hp, hp],
                 'Strength': roll_die(3, 6), 'Dexterity': roll_die(3, 6), 'Constitution': roll_die(3, 6),
                 'Intelligence': roll_die(3, 6), 'Wisdom': roll_die(3, 6), 'Charisma': roll_die(3, 6),
                 'XP': 0, 'Inventory': []}
    return character


def roll_hp(character_class):
    """
    Generate a random number based on the class the user selected.

    :precondition: the class must be properly formatted string
    :post condition: determine's a character's HP as an integer
    :param character_class: the character's class as a string
    :return: a random number as an integer
    """
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


def get_character_name(syllables):
    """
    Generate a name base on a given amount of syllables.

    :precondition: the function will only work for positive non-zero integers
    :post condition: return a string of letters alternating vowels and consonants
    :param syllables: an integer
    :return: a concatenated string of random letters
    """
    string = ""
    for x in range(0, syllables):
        string = string + generate_syllable()
    return string.capitalize()


def generate_vowel():
    """
    Generate a random vowel.
    :return: a random vowel character
    """
    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    random_selection = random.choice(vowel)
    return random_selection


def generate_consonant():
    """
    Generate a random consonant.
    :return: a random consonant character
    """
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    random_selection = random.choice(consonant)
    return random_selection


def generate_syllable():
    """
    Generate a random syllable.
    :return: a random syllable as a concatenated string
    """
    vowel = generate_vowel()
    consonant = generate_consonant()
    syllable = consonant + vowel
    return syllable


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
    attributes = ['Name', 'Race', 'Class', 'HP', 'Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma', 'XP', 'Inventory']
    for index in range(0, len(attributes)):
        print(f"{attributes[index]}: {character[attributes[index]]}")

    if len(character['Inventory']) == 11:
        for index in range(0, len(attributes) - 2):
            print(f"{attributes[index]}: {character[attributes[index]]}")
        # print(f"Name: {character['Name']}")
        # print(f"Race: {character['Race']}")
        # print(f"Class: {character['Class']}")
        # print(f"HP: {character['HP'][1]}/{character['HP'][0]}")
        # print(f"Strength: {character['Strength']}")
        # print(f"Dexterity: {character['Dexterity']}")
        # print(f"Constitution: {character['Constitution']}")
        # print(f"Intelligence: {character['Intelligence']}")
        # print(f"Wisdom: {character['Wisdom']}")
        # print(f"Charisma: {character['Charisma']}")
        # print(f"Experience: {character['XP']}")
    elif len(character['Inventory']) > 0:
        for index in range(0, len(attributes) - 2):
            print(f"{attributes[index]}: {character[attributes[index]]}")
        # print(f"Name: {character['Name']}")
        # print(f"Race: {character['Race']}")
        # print(f"Class: {character['Class']}")
        # print(f"HP: {character['HP'][1]}/{character['HP'][0]}")
        # print(f"Strength: {character['Strength']}")
        # print(f"Dexterity: {character['Dexterity']}")
        # print(f"Constitution: {character['Constitution']}")
        # print(f"Intelligence: {character['Intelligence']}")
        # print(f"Wisdom: {character['Wisdom']}")
        # print(f"Charisma: {character['Charisma']}")
        # print(f"Experience: {character['XP']}")
        # print("--Here are your inventory items--")
        for length in range(0, len(character['Inventory'])):
            print(character['Inventory'][length])

    elif len(character) != 12:
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


def combat_round(opponent_one, opponent_two):
    roll_opponent_one = 0
    roll_opponent_two = 0
    while roll_opponent_one == roll_opponent_two:
        roll_opponent_one = roll_die(1,20)
        roll_opponent_two = roll_die(1, 20)
    if roll_opponent_one > roll_opponent_two:
        print(f"{opponent_one['Name']} will attack first.")
        attack_roll_one = roll_die(1, 20)
        print(f"{opponent_one['Name']} will attack with {attack_roll_one} towards {opponent_two['Name']}")
        if attack_roll_one > opponent_two['Dexterity']:
            print(f"{opponent_two['Name']} has fallen. {opponent_one['Name']} has won!")
        else:
            print(f"{opponent_two['Name']} has countered the attack!")
    elif roll_opponent_one < roll_opponent_two:
        print(f"{opponent_two['Name']} will attack first.")
        attack_roll_two = roll_die(1, 20)
        print(f"{opponent_two['Name']} will attack with {attack_roll_two} towards {opponent_one['Name']}")
        if attack_roll_two > opponent_one['Dexterity']:
            print(f"{opponent_one['Name']} has fallen. {opponent_two['Name']} has won!")
        else:
            print(f"{opponent_one['Name']} has countered the attack!")


if __name__ == '__main__':
    # doctest.testmod()
    # print(select_race())

    new_character = create_character()
    print_character(new_character)
    test = choose_inventory()
    new_character["Inventory"] = test
    print_character(new_character)

    # combat_round({'Name': 'Katherine', 'Race': 'gnome', 'Class': 'druid', 'HP': [4, 4], 'Strength': 12, 'Dexterity': 10, 'Constitution': 15, 'Intelligence': 13, 'Wisdom': 5, 'Charisma': 8, 'XP': 0},
    #               {'Name': 'Marlon', 'Race': 'gnome', 'Class': 'druid', 'HP': [4, 4], 'Strength': 12, 'Dexterity': 14,
    #                'Constitution': 15, 'Intelligence': 13, 'Wisdom': 5, 'Charisma': 8, 'XP': 0})

    # character = {'Name': get_character_name(6), 'Race': 'gnome', 'Class': 'druid', 'HP': [4, 4], 'Strength': 12, 'Dexterity': 10, 'Constitution': 15, 'Intelligence': 13, 'Wisdom': 5, 'Charisma': 8, 'XP': 0}
    # attributes = ['Name', 'Race', 'Class', 'HP', 'Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom',
    #               'Race', 'Charisma', 'XP']
    # for index in range(0, len(attributes)):
    #     print(f"{attributes[index]}: {character[attributes[index]]}")