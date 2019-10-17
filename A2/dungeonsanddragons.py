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

    User will be asked for input for the available items.

    Will show items sold, will stop asking for input when user enters (-1) or if the shop runs out of items.
    :return: a list
    """
    shop_items = {1: 'sword', 2: 'dagger', 3: 'battleaxe', 4: 'spear', 5: 'quarterstaff', 6: 'shield', 7: 'potion '}
    shop_items_sold = shop_items.copy()
    item_selection = 0
    items = []
    print("\n -----Welcome to the Olde Tyme Merchant!-----\n\nHere is what we have for sale:\n")
    while item_selection != -1 and len(shop_items) > 0:
        for x in range(1, 8):
            print(f"{x}. {shop_items_sold[x]}")
        item_selection = int(input("Enter the number of the item you would like to buy (-1 to finish shopping)\n"))
        if 7 >= item_selection > 0:
            item = shop_items[item_selection]
            del shop_items[item_selection]
            items.append(item)
            shop_items_sold[item_selection] = 'Sold'
        elif len(shop_items) == 0:
            item_selection = -1
        else:
            print("Invalid entry. Please select from the available items (by number).\n")
    print("Thank you for shopping, here are your items.")
    return items


def create_character(name_length):
    """
    Create a dictionary including attributes to associate to a character.

    :post condition: will create a character as a dictionary of attributes
    :return: the information of a character as a dictionary
    """
    char_class = select_class()
    hp = roll_hp(char_class)
    character = {'Name': get_character_name(name_length//2), 'Race': select_race(), 'Class': char_class, 'HP': [hp, hp],
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
    if character['Inventory'] == []:
        for index in range(0, len(attributes) - 1):
            print(f"{attributes[index]}: {character[attributes[index]]}")
    elif len(character['Inventory']) > 0:
        for index in range(0, len(attributes) - 1):
            print(f"{attributes[index]}: {character[attributes[index]]}")

        print("Here are your items:")
        for length in range(0, len(character['Inventory'])):
            print(character['Inventory'][length])
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


def combat_round(opponent_one, opponent_two):
    """
    Simulate a round of combat between two created characters.

    Call attack function to simulate an attack.

    Print the outcome of the round.
    :precondition: both parameters must be properly formatted character dictionaries
    :param opponent_one: a dictionary with character information
    :param opponent_two: a dictionary with character information
    """
    roll_opponent_one = 0
    roll_opponent_two = 0
    while roll_opponent_one == roll_opponent_two:
        roll_opponent_one = roll_die(1,20)
        roll_opponent_two = roll_die(1, 20)
    if roll_opponent_one > roll_opponent_two:
        opponent_two['HP'][1] = attack(opponent_one, opponent_two)
        if opponent_two['HP'][1] > 0:
            attack(opponent_two, opponent_one)

    elif roll_opponent_one < roll_opponent_two:
        opponent_one['HP'][1] = attack(opponent_two, opponent_one)
        if opponent_one['HP'][1] > 0:
            attack(opponent_one, opponent_two)


def attack(first_attacker, second_attacker):
    """
    Simulate an attack between two opponents.
    :param first_attacker: a dictionary with character information
    :param second_attacker: a dictionary with character information
    :return: the outcome of the attack
    """
    print(f"{first_attacker['Name']} will attack.")
    print("They are now rolling the die.....")
    attack_roll_one = roll_die(1, 20)
    print(f"{first_attacker['Name']} will attack {second_attacker['Name']} with {attack_roll_one} damage!")
    if attack_roll_one > second_attacker['Dexterity']:
        current_hp = second_attacker['HP'][1] - attack_roll_one
        if current_hp > 0:
            print(f"{second_attacker['Name']} anticipated the attack! {second_attacker['Name']} now has {current_hp}HP")
            return current_hp
        if current_hp <= 0:
            print(f"{second_attacker['Name']} was killed in battle")
            return current_hp
    elif attack_roll_one < second_attacker['Dexterity']:
        print(f"It missed! {second_attacker['Name']} anticipated the attack!")
        return second_attacker['HP'][1]


if __name__ == '__main__':
    # doctest.testmod()
    # print(select_race())

    # new_character = create_character(8)
    # print_character(new_character)
    # test = choose_inventory()
    # print(test)

    # new_character_one["Inventory"] = test
    # print_character(new_character)

    combat_round(create_character(8), create_character(8))

