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

    :return: a list of user-selected items
    """
    shop_items = {1: 'sword', 2: 'dagger', 3: 'battleaxe', 4: 'spear', 5: 'quarterstaff', 6: 'shield', 7: 'potion '}
    item_selection = 0
    items = []
    print("\n -----Welcome to the Olde Tyme Merchant!-----\n\nHere is what we have for sale:\n")
    while item_selection != -1:
        for x in range(1, 8):
            print(f"{x}. {shop_items[x]}")
        item_selection = int(input("Enter the number of the item you would like to buy (-1 to finish shopping)\n"))
        if 7 >= item_selection > 0:
            item = shop_items[item_selection]
            items.append(item)
        elif item_selection == -1:
            continue
        else:
            print("Invalid entry. Please select from the available items (by number).\n")

    print("Thank you for shopping.")
    return items


def create_character(name_length):
    """
    Create a dictionary including attributes to associate to a character.

    :post condition: will create a character as a dictionary of attributes
    :return: the information of a character as a dictionary
    """
    char_class = select_class()
    hp = roll_hp(char_class)
    character = {'Name': get_character_name(name_length//2), 'Race': select_race(), 'Class': char_class,
                 'HP': [hp, hp], 'Strength': roll_die(3, 6),
                 'Dexterity': roll_die(3, 6), 'Constitution': roll_die(3, 6), 'Intelligence': roll_die(3, 6),
                 'Wisdom': roll_die(3, 6), 'Charisma': roll_die(3, 6), 'XP': 0, 'Inventory': []}
    return character


def roll_hp(character_class):
    """
    Generate a random number based on the class the user selected.

    :precondition: the class must be properly formatted string
    :post condition: determine's a character's HP as an integer
    :param character_class: the character's class as a string
    :return: a random number as an integer
    """
    dict_of_classes = {'barbarian': roll_die(1, 12), 'bard': roll_die(1, 8), 'cleric': roll_die(1, 8),
                       'druid': roll_die(1, 8), 'monk': roll_die(1, 8), 'rogue': roll_die(1, 8), 'warlock': roll_die(1, 8),
                       'fighter': roll_die(1, 10), 'paladin': roll_die(1, 10), 'ranger': roll_die(1, 10),
                       'sorcerer': roll_die(1, 6), 'wizard': roll_die(1, 6)}
    if character_class in dict_of_classes:
        return dict_of_classes[character_class]
    else:
        return 'Error in inputted class.'


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
    >>> print_character({'Name': 'Qumerate', 'Race': 'gnome', 'Class': 'monk', 'HP': [5, 5], 'Strength': 11, 'Dexterity': 12, 'Constitution': 10, 'Intelligence': 11, 'Wisdom': 10, 'Charisma': 13, 'XP': 0, 'Inventory': ['Hello','World']})
    Name: Qumerate
    Race: gnome
    Class: monk
    HP: [5, 5]
    Strength: 11
    Dexterity: 12
    Constitution: 10
    Intelligence: 11
    Wisdom: 10
    Charisma: 13
    XP: 0
    Here are your items:
    Hello
    World
    """
    attributes = ['Name', 'Race', 'Class', 'HP', 'Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma', 'XP', 'Inventory']
    if character['Inventory'] == []:
        for index in range(0, len(attributes) - 1):
            print(f"{attributes[index]}: {character[attributes[index]]}")
    elif 7 > len(character['Inventory']) > 0:
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
    print(f"\nA battle is ensues between two warriors, {opponent_one['Name']} the {opponent_one['Class']} and {opponent_two['Name']} the {opponent_two['Class']}...")
    print(f"The {opponent_one['Class']} lets out a war cry: \'ONE SHALL STAND, ONE SHALL FALL!\' ")
    roll_opponent_one = 0
    roll_opponent_two = 0
    while roll_opponent_one == roll_opponent_two:
        roll_opponent_one = roll_die(1, 20)
        roll_opponent_two = roll_die(1, 20)
    if roll_opponent_one > roll_opponent_two:
        opponent_two['HP'][1] = attack(opponent_one, opponent_two)
        if opponent_two['HP'][1] > 0:
            opponent_one['HP'][1] = attack(opponent_two, opponent_one)
    elif roll_opponent_one < roll_opponent_two:
        opponent_one['HP'][1] = attack(opponent_two, opponent_one)
        if opponent_one['HP'][1] > 0:
            opponent_two['HP'][1] = attack(opponent_one, opponent_two)


def attack(attacker, recipient):
    """
    Simulate an attack between two opponents.

    :param attacker: a dictionary with character information
    :param recipient: a dictionary with character information
    :return: the remaining hp o
    """
    print(f"{attacker['Name']} will attack.\nThey are now rolling the die.....")
    attack_roll_one = roll_die(1, 20)
    attack_damage = roll_hp(attacker['Class'])
    print(f"{attacker['Name']} will attack {recipient['Name']} with {attack_damage} damage!")
    recipient['HP'][1] = check_dexterity(attack_roll_one, recipient, attack_damage)
    return recipient['HP'][1]


def check_dexterity(attack_roll, defender, damage):
    if attack_roll > defender['Dexterity']:
        current_hp = defender['HP'][1] - damage
        if current_hp > 0:
            print(f"{defender['Name']} took the blow! Pain travels through his veins as he tries to collect himself. {defender['Name']} now has {current_hp}HP")
            return current_hp
        if current_hp <= 0:
            print(f"{defender['Name']} was slain in battle! He had no chance to defend himself.")
            return 0
    elif attack_roll < defender['Dexterity']:
        print(f"It missed! {defender['Name']} anticipated the attack!")
        return defender['HP'][1]


def main():
    doctest.testmod()
    # Create first character
    new_character_one = create_character(8)
    print(new_character_one)
    test = choose_inventory()
    print(test)
    print_character(new_character_one)
    # Create second character
    new_character_two = create_character(8)
    test = choose_inventory()
    print(test)
    print_character(new_character_two)
    # Pin the two characters against each other
    combat_round(new_character_one, new_character_two)


if __name__ == '__main__':
    main()
