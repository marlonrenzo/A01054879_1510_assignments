from A3.character import create_character
from A3.monster import new_monster
import random


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


def validate_move(coordinates: dict, direction: str) -> bool:
    """
    Validate that the move will be within the 5x5 limits.

    :param coordinates: a dictionary
    :param direction: an int
    :precondition: coordinates must be a dictionary with x and y coordinates
    :precondition: direction must be a string
    :post condition: will return the validity of the move as a boolean
    :return: a boolean
    >>> validate_move({"x": 0, "y": 2}, 4)
    True
    >>> validate_move({"x": 0, "y": 4}, 2)
    False
    >>> validate_move({"x": 4, "y": 2}, 4)
    False
    >>> validate_move({"x": 3, "y": 2}, 4)
    True
    """
    if (coordinates["x"] == 4 and direction == 'd') or (coordinates["x"] == 0 and direction == 'a'):
        return False
    elif (coordinates["y"] == 4 and direction == 's') or (coordinates["y"] == 0 and direction == 'w'):
        return False
    else:
        return True


def move_character(coordinates: dict, direction: str) -> dict:
    """
    Update coordinates based on the direction.
    :param coordinates: a dictionary
    :param direction: an int
    :precondition: coordinates must be a dictionary with x and y coordinates
    :precondition: direction must be an integer between 1 - 4 inclusive
    :post condition: will return updated coordinates after the move
    :return: a dictionary
    >>> move_character({"x": 0, "y": 0}, 4)
    {'x': 1, 'y': 0}
    >>> move_character({"x": 3, "y": 3}, 1)
    {'x': 3, 'y': 2}
    >>> move_character({"x": 1, "y": 1}, 3)
    {'x': 0, 'y': 1}
    >>> move_character({"x": 0, "y": 1}, 1)
    {'x': 0, 'y': 0}
    """
    moves = {'w': -1, 's': 1, 'a': -1, 'd': 1}
    if direction == 1 or direction == 2:
        coordinates["y"] += moves[direction]
    if direction == 3 or direction == 4:
        coordinates["x"] += moves[direction]
    return coordinates


def get_move() -> str:
    """
    Ask the user for the direction of a move.

    :return: an int
    """
    user_move = input("Where do you want to move? North[W], South[S], East[D], West[A] or 'quit'")
    return user_move.lower()


def print_position(position):
    """
    Show the current position based on the coordinates.

    Print out a 5x5 of squares[ ] and keep checking if the user is located at each square with check_position.

    Use a nested loop; one loop to print each row, and the nested loop to print each column in each row.
    :param position: a dictionary
    :precondition: position must be a dictionary
    :post condition: will print the location of the user
    """
    place_holder = ["[ ]", "[x]"]
    for y_axis in range(5): # create the 5 rows
        print("\n")
        for x_axis in range(5): # create the 5 columns each row
            # Print the correct place holder within place_holder by the output produced by check_position
            print(place_holder[check_position(position, x_axis, y_axis)], end=" ")
    print("\n")


def check_position(position, x_position, y_position):
    """
    Check position to determine if the character is located at the coordinates.

    :param position: a dictionary
    :param x_position: an integer
    :param y_position: an integer
    :precondition: position must be a dictionary
    :precondition: x_position and y_position must be integers
    :post condition: will determine whether or not the user is located at the specified coordinates with a 1 or a 0
    :return: an integer
    """
    if position["x"] == x_position and position["y"] == y_position:
        return 1
    else:
        return 0


def twenty_five_percent_chance() -> bool:
    """
    Generate a random number between 1 and 4 exclusive, compare the random number to 2 and return a boolean.

    Creates a 25% chance to return true.
    :return: a boolean
    """
    chance = random.randint(1, 4)
    if chance == 2:
        return True
    else:
        return False


def battle(character, monster):
    rounds = 0
    round_cases = ["\nA battle ensues. Tension rises. Prepare for blood and despair."]
    while character["HP"][0] > 0 and monster["HP"][0] > 0:
        if get_user_choice_battle() == 1:
            round_cases.append("\nThe battle continues.....")
            print(round_cases[rounds])
            remaining_health = combat_round(character, monster)
            character['HP'][0] = remaining_health[0]
            monster['HP'][0] = remaining_health[1]
            rounds += 1
            monster_drops_key = twenty_five_percent_chance()
            if monster_drops_key:
                print('The monster dropped a key!')
                character['Inventory'].append('key')
        else:
            break
    return character


def combat_round(character, monster):
    attacks_first = [[character, monster], [monster, character]]  # generates cases where either of them attack first
    random_attacker = random.randint(0, 1)  # will determine which case to use in first_attacker
    attacker = attacks_first[random_attacker]
    attacker[1]['HP'][0] = attack(attacker[0], attacker[1])  # sets the hp of recipient to whatever attack returns
    if check_alive(attacker[1]):  # if the recipient of the attack is still alive, they will attack back
        attacker[0]['HP'][0] = attack(attacker[1], attacker[0])  # invokes attack function, switches order of attacker
    return [character["HP"][0], monster["HP"][0]]


def attack(attacker: dict, recipient: dict) -> int:
    """
    Simulate an attack between two opponents.

    :param attacker: a dictionary with character information
    :param recipient: a dictionary with character information
    :return: an int
    """
    attack_outcome = ["The attack was successful! The strike dealt significant damage!", "The attack missed!"]
    random_outcome = random.randint(0, 1)  # choose a random outcome
    print(f"{attacker['Alias']} will attack.\nNow rolling the die.....")
    attack_roll = roll_die(1, 6)  # Determine the damage an attack deals
    print(f"{attacker['Alias']} will attack {recipient['Alias']} with {attack_roll} damage!")
    print(attack_outcome[random_outcome])  # prints the random outcome of an attack (hit or miss)
    if not random_outcome:  # if attack is successful
        remaining_hp = recipient['HP'][0] - attack_roll
        print(f"The hit left {recipient['Alias']} with {remaining_hp}/{recipient['HP'][1]} HP")
        return remaining_hp
    else:
        return recipient['HP'][0]  # original HP


def check_alive(character):
    """
    Check a character's health
    :param character:
    :return:
    """
    if character['HP'][1] < 0:
        # print(f"As sad as it may be {character['Name']}, you have died and will flourish in the afterlife. "
        #       f"Try playing again")
        return False
    else:
        return True


def startup():
    """
    Print the startup scenario.
    """
    print("You are awoken in a dark concrete room. Doors surround you on all sides.\n"
          "A trap door in the middle of the room protrudes the ceiling. It requires a key. \n"
          "You observe the empty room some more.\nWords scratched against the walls - 'ESCAPE'.\n"
          "Find the key.")


# def print_dictionary(dictionary: dict):
#     for x in dictionary.keys():
#         print(f"{x}: {dictionary[x]}")


def get_user_choice_battle() -> bool:
    """
    Grab user input to determine if they want to run from or fight monster.
    :return: a boolean
    """
    user_input = bool(input("Would you like to fight[1] or run[0]?"))
    return user_input


def heal(health):
    if health < 9:
        health += 2
        print(f"Whilst moving around, you have healed a bit. You're now at {health}/10 HP ")
    elif health == 9:
        health += 1
        print(f"Whilst moving around, you have healed a bit. You're now at {health}/10 HP ")
    return health


def check_at_exit_with_key(position, inventory):
    if position['x'] == 4 and position['y'] == 4 and inventory == ['key']:
        return True
    else:
        return False


def user_win():
    print("Greatest salutations young lad! You've escaped the Kather's tunnels! You will make a noble warrior one day!")
    return


def run_game():
    character = create_character()
    startup()
    character_is_alive = check_alive(character)
    while character_is_alive:
        print_position(character["position"])
        direction = get_move()
        valid_move = validate_move(character['position'], direction)
        if direction == 'quit':
            print('K bye.')
            break
        elif valid_move:
            character["position"] = move_character(character["position"], direction)
            character["HP"][0] = heal(character["HP"][0])
            character_escape = check_at_exit_with_key(character['position'], character['Inventory'])
            if character_escape:
                user_win()
                break
            monster_encounter = twenty_five_percent_chance()
            if monster_encounter:
                monster = new_monster()
                character = battle(character, monster)
                character_is_alive = check_alive(character)
        else:
            print("Cannot go any further, there is a wall there. Try moving in another direction")

if __name__ == "__main__":
    run_game()
    # character = create_character()
    # character = check_the_room(character)
    # print(battle({'Name': 'Marlon', 'Alias': 'You', 'Class': 'Wizard', 'HP': [10, 10], 'Inventory': [], 'Spells': [],
    #             'position': {"x": 2, "y": 2}, "Attack Roll": 0},
    #             {'Alias': "The Monster", 'HP': [5, 5], "Attack Roll": 0}))

    # a = {'Name': 'Marlon', 'Alias': 'You', 'Class': 'Wizard', 'HP': [10, 10], 'Inventory': [], 'Spells': [],
    #  'position': {"x": 2, "y": 2}, "Attack Roll": 0}
    # print(f"{a['Alias']}")