def get_character_name():
    """
    Inquire the user to provide a name.

    :return: a string
    """
    name = input("What is your name?").capitalize()
    print(f"Nice to meet you {name}\n")
    return name


def create_character() -> dict:
    """
    Create a dictionary including attributes to associate to a character.

    :post condition: will create a character as a dictionary of attributes
    :return: the information of a character as a dictionary
    """
    print("\nWelcome to the Dungeon of Kather. 'Ere are where young lads, like yourself, learn to become a warrior.\n"
          "It is tradition at Castor's Thrine that all younglings are placed within the walls of Kather to begin training.\n"
          "The Dungeon has 25 rooms for you to traverse through and eventually escape. Go forth and slash your way through \n"
          "young blood-seeker. There are monsters in this realm. Escape the dungeon with your life and you will be unstoppable.\n\n"
          "Let's begin by getting to know you.........")
    character = {'Name': get_character_name(), 'Alias': "You", 'HP': [10, 10], 'Inventory': [], 'position': {"x": 2, "y": 2}}
    return character

# Test dictionary: {'Name': 'Marlon', 'Alias': 'You', 'Class': 'Wizard', 'HP': [10, 10], 'Inventory': [], 'Spells': [], 'position': {"x": 2, "y": 2}, "Attack Roll": 0}
