from A3.SUD import roll_die


def create_character(name_length):
    """
    Create a dictionary including attributes to associate to a character.

    :post condition: will create a character as a dictionary of attributes
    :return: the information of a character as a dictionary
    """
    print("\n\n\nLet's create a character\nStart by selecting a class.\n")
    char_class = select_class()
    hp = roll_hp(char_class)
    character = {'Name': get_character_name(), 'Race': select_race(), 'Class': char_class,
                 'HP': [hp, hp], 'Strength': roll_die(3, 6),
                 'Dexterity': roll_die(3, 6), 'Constitution': roll_die(3, 6), 'Intelligence': roll_die(3, 6),
                 'Wisdom': roll_die(3, 6), 'Charisma': roll_die(3, 6), 'XP': 0, 'Inventory': []}
    return character


def get_character_name():
    """
    Inquire the user to provide a name.

    :return: a string
    """
    string = input("What is your name?")
    return string.capitalize()


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