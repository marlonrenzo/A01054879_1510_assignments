def get_character_name():
    """
    Inquire the user to provide a name.

    :return: a string
    """
    name = input("What is your name?").capitalize()
    print(f"Nice to meet you {name}\n")
    return name


def create_character():
    """
    Create a dictionary including attributes to associate to a character.

    :post condition: will create a character as a dictionary of attributes
    :return: the information of a character as a dictionary
    """
    print("\nWelcome to the Dungeon of Kather. Here are where young wizards, like yourself, learn new spells.\n"
          "It is tradition at Castor's Thrine of Enchantment that all younglings are placed within the walls\n"
          "of Kather to begin training. The Dungeon has 25 rooms for you to traverse through and eventually escape.\n"
          "Use your knowledge as a spell-caster and use any items you think are useful.\n\n"
          "Let's begin by getting to know you.........")
    character = {'Name': get_character_name(), 'Class': 'Wizard', 'HP': [10, 10], 'Inventory': [], 'Spells': []}
    return character