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


def validate_move(coordinates: dict, direction: int) -> bool:
    """
    Validate that the move will be within the 5x5 limits.

    :param coordinates: a dictionary
    :param direction: an int
    :precondition: coordinates must be a dictionary with x and y coordinates
    :precondition: direction must be an integer between 1 - 4 inclusive
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
    if (coordinates["x"] == 4 and direction == 4) or (coordinates["x"] == 0 and direction == 3):
        return False
    elif (coordinates["y"] == 4 and direction == 2) or (coordinates["y"] == 0 and direction == 1):
        return False
    else:
        return True


def move(position):
    direction = get_move()
    if direction == 5:
        print("Thanks for playing!")
    else:
        valid_move = validate_move(position, direction)
        if valid_move:
            position = move_character(position, direction)
        else:
            print("Cannot go any further, there is a wall there. Try moving in another direction")
    return position


def move_character(coordinates: dict, direction: int) -> dict:
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
    moves = {1: -1, 2: 1, 3: -1, 4: 1}
    if direction == 1 or direction == 2:
        coordinates["y"] += moves[direction]
    if direction == 3 or direction == 4:
        coordinates["x"] += moves[direction]
    return coordinates


def get_move() -> int:
    """
    Ask the user for the direction of a move.

    :return: an int
    """
    move = int(input("Where do you want to move?\n1: up\n2: down\n3: left\n4: right\n5: quit\n"))
    return move


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
    for y_axis in range(5):
        # create the 5 rows
        print("\n")
        for x_axis in range(5):
            # create the 5 columns each row
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


def check_for_monster() -> bool:
    encounter_chance = random.randint(0, 4)
    if encounter_chance == 2:
        return True
    else:
        return False


# def battle(character, monster):
#     while character["HP"] > 0 and monster["HP"] > 0:
#         character["HP"][0] = combat_round(character, monster)
#
#
# def combat_round(character, monster):
#
#     character_roll = [character, roll_die(1, 6)]
#     monster_roll = [monster, roll_die(1, 6)]
#     while character_roll[1] == monster_roll[1]:
#         character_roll[1] = roll_die(1, 6)
#         monster_roll[1] = roll_die(1, 6)
#
#     if character_roll > monster_roll:
#         attack
#     return character["HP"][0]
#
# def attack(attacker, recipient):
#     """
#     Simulate an attack between two opponents.
#
#     :param attacker: a dictionary with character information
#     :param recipient: a dictionary with character information
#     :return:
#     """
#     print(f"{attacker['Name']} will attack.\nNow rolling the die.....")
#     attack_roll_one = roll_die(1, 6)
#     print(f"{attacker['Name']} will attack {recipient['Name']} with {attack_roll_one} damage!")
#     return recipient['HP'][1]


def startup():
    """
    Print the startup scenario.
    """
    print("You are awoken in a dark concrete room. Doors surround you on all sides.\n"
          "A trap door in the middle of the room protrudes the ceiling. It requires a key. \n"
          "You observe the empty room some more.\nWords scratched against the walls - 'ESCAPE'.\n")


def run_game():
    character = create_character()
    startup()
    while True:
        actions = {1: ["Move", move], 0: ["Quit"]}
        print_position(character["position"])

        for x in actions.keys():
            print(f"{x}: {actions[x][0]}")
        user_action = int(input("\nWhat would you like to do?"))
        if user_action == 1:
            character["position"] = move(character["position"])
            monster_encounter = check_for_monster()
            if monster_encounter:
                monster = new_monster()
                # character["HP"][0] = battle(character, monster)
                print(f"Monster appeared! It has HP of {monster['HP'][1]}")
        elif not user_action:
            print("Thanks for playing!")
            break
        else:
            print("That was not a valid entry. Please try again.")


if __name__ == "__main__":
    run_game()

