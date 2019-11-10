from A3.character import create_character
from A3.monster import new_monster
import doctest
import random


def roll_die(number_of_rolls: int, number_of_sides: int) -> int:
    """
    Return a random positive integer base on the parameters.

    :param number_of_rolls: an integer
    :param number_of_sides: an integer
    :precondition: both parameters must be positive.
    :post condition: will return a sum of x amount of rolls on a y-sided die
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

    Check if the position is the at both x and y boundaries and if they are crossing the boundaries.

    :param coordinates: a dictionary
    :param direction: a string
    :precondition: coordinates must be a dictionary with x and y coordinates
    :precondition: direction must be a string
    :post condition: will return the validity of the move as a boolean
    :return: a boolean

    >>> validate_move({"x": 0, "y": 2}, 'd')
    True
    >>> validate_move({"x": 0, "y": 4}, 's')
    False
    >>> validate_move({"x": 4, "y": 2}, 'd')
    False
    >>> validate_move({"x": 3, "y": 2}, 'd')
    True
    """
    if (coordinates["x"] == 4 and direction == 'd') or (coordinates["x"] == 0 and direction == 'a') or \
       (coordinates["y"] == 4 and direction == 's') or (coordinates["y"] == 0 and direction == 'w'):
        return False  # user does not input a valid move if they try to cross a boundary
    else:
        return True  # user move is valid if none of the boundaries are crossed


def move_character(coordinates: dict, direction: str) -> dict:
    """
    Update coordinates based on the direction.

    Add the number to coordinates by accessing the correct number in available_moves.

    :param coordinates: a dictionary
    :param direction: an int
    :precondition: coordinates must be a dictionary with x and y coordinates
    :precondition: direction must be an integer between 1 - 4 inclusive
    :post condition: will return updated coordinates after the move
    :return: a dictionary

    >>> move_character({"x": 0, "y": 0}, 'd')
    {'x': 1, 'y': 0}
    >>> move_character({"x": 3, "y": 3}, 'w')
    {'x': 3, 'y': 2}
    >>> move_character({"x": 1, "y": 1}, 'a')
    {'x': 0, 'y': 1}
    >>> move_character({"x": 0, "y": 1}, 's')
    {'x': 0, 'y': 2}
    """
    available_moves = {'w': -1, 's': 1, 'a': -1, 'd': 1}  # a dictionary that will change coordinates based on the key
    if direction == 'w' or direction == 's':  # change the y coordinate if user wants to move up or down
        coordinates["y"] += available_moves[direction]
    if direction == 'a' or direction == 'd':  # change teh x coordinate if the user wants to move left or right
        coordinates["x"] += available_moves[direction]
    return coordinates


def get_move() -> str:
    """
    Ask the user for the direction of a move.

    :return: an int

    """
    user_move = input("Where do you want to move? North[W], South[S], East[D], West[A] or 'quit'")
    return user_move.lower()


def print_position(position: dict):
    """
    Show the current position based on the coordinates.

    Print out a 5x5 of squares[ ] and keep checking if the user is located at each square with check_position.

    Use a nested loop; one loop to print each row, and the nested loop to print each column in each row.
    :param position: a dictionary
    :precondition: position must be a dictionary
    :post condition: will print the location of the user
    :return: nothing

    """
    place_holder = ["[ ]", "[x]"]
    for y_axis in range(5): # create the 5 rows
        print("\n")
        for x_axis in range(5): # create the 5 columns each row
            # Print the correct place holder within place_holder by the output produced by check_position
            print(place_holder[check_position(position, x_axis, y_axis)], end=" ")
    print("\n")
    return


def check_position(position: dict, x_position: int, y_position: int) -> bool:
    """
    Check position to determine if the character is located at the coordinates.

    :param position: a dictionary
    :param x_position: an integer
    :param y_position: an integer
    :precondition: position must be a dictionary
    :precondition: x_position and y_position must be integers
    :post condition: will determine whether or not the user is located at the specified coordinates with a 1 or a 0
    :return: an integer

    >>> check_position({"x": 0, "y": 1}, 0, 1)
    True
    >>> check_position({"x": 4, "y": 4}, 4, 4)
    True
    >>> check_position({"x": 2, "y": 2}, 0, 0)
    False
    """
    if position["x"] == x_position and position["y"] == y_position:
        return True  # return True if the position and the coordinates provided are equal
    else:
        return False


def one_in_x_chance(x: int) -> bool:
    """
    Generate a random number between 1 and x inclusive, compare the random number to x and return a boolean.

    Creates a 25% chance to return true.
    :return: a boolean

    """
    chance = random.randint(1, x)
    if chance == x:
        return True
    else:
        return False


def battle(character: dict, monster: dict) -> dict:
    """
    Simulate a battle between character and monster.

    Update character information based on the outcome of each round of combat.

    Create a 1 in 4 chance that the monster will drop a key when killed.

    :param character: a dict
    :param monster: a dict
    :precondition: character must be a properly formed dictionary
    :precondition: monster must be a properly formed dictionary
    :post condition: will return an updated character based on tbe outcome of the battle
    :return: a dict

    """
    rounds = 0  # a variable to keep track how many rounds
    round_cases = ["\nA battle ensues. Tension rises. Prepare for blood and despair."]  # what displays to begin a round
    while character["HP"][0] > 0 and monster["HP"][0] > 0:  # loop to simulate combat rounds while both character alive
        round_cases.append("\nThe battle continues.....")  # will show this on screen when rounds are more than 0
        print(round_cases[rounds])  # print the right case based on what round it is
        remaining_health = combat_round(character, monster)  # simulate a round assigning the result to a list
        character['HP'][0] = remaining_health[0]  # update the character's health by assigning combat_round's result
        monster['HP'][0] = remaining_health[1]  # update the character's health by assigning combat_round's result
        rounds += 1  # show that the round will increase
    if one_in_x_chance(4) and character['HP'][0]:  # 1 in 4 chance for the monster to drop key if character is not dead
        print('The monster dropped a key!')
        character['Inventory'].append('key')  # add a key to character's inventory
    print(f"Your HP is now at {character['HP'][0]}/{character['HP'][1]}")  # print out the remaining character health
    return character


def combat_round(character: dict, monster: dict) -> list:
    """
    Simulate a combat round between character and a monster.

    Generate a random order of attack by using a nested list.

    Return the updated HP of character and monster after the round occurs.
    :param character: a dict
    :param monster: a dict
    :precondition: character must be a properly formed dictionary
    :precondition: monster must be a properly formed dictionary
    :post condition: will return a list of updated HPs of character and monster
    :return: a list

    """
    attacks_first = [[character, monster], [monster, character]]  # generates cases where either characters attack first
    random_attacker = random.randint(0, 1)  # will determine which case to use in first_attacker above
    attacker = attacks_first[random_attacker]  # initializes a variable to refer to the case used
    attacker[1]['HP'][0] = attack(attacker[0], attacker[1])  # sets the hp of recipient to whatever attack returns
    if check_alive(attacker[1]):  # if the recipient of the attack is still alive, they will attack back
        attacker[0]['HP'][0] = attack(attacker[1], attacker[0])  # invokes attack function, switches order of attacker
    return [character["HP"][0], monster["HP"][0]]


def attack(attacker: dict, recipient: dict) -> int:
    """
    Simulate an attack between two opponents.

    :param attacker: a dictionary with character information
    :param recipient: a dictionary with character information
    :precondition: attacker must be a properly formed dictionary
    :precondition: recipient must be a properly formed dictionary
    :post condition: will return HP of the recipient
    :return: an int

    """
    attack_outcome = ["The attack was successful! The strike dealt significant damage!", "The attack missed!"]  # possible outcomes of an attack
    random_outcome = random.randint(0, 1)  # choose a random outcome
    print(f"{attacker['Alias']} will attack.\nNow rolling the die.....")
    attack_roll = roll_die(1, 6)  # Determine the damage an attack deals
    print(f"{attacker['Alias']} will attack {recipient['Alias']} with {attack_roll} damage!")
    print(attack_outcome[random_outcome])  # prints the random outcome of an attack (hit or miss)
    if not random_outcome:  # if attack is successful
        remaining_hp = recipient['HP'][0] - attack_roll  # subtract damage from the recipient's HP
        print_remaining_hp(recipient, remaining_hp)  # print remaining HP
        return remaining_hp
    else:
        return recipient['HP'][0]  # original HP


def print_remaining_hp(entity: dict, remaining_hp: int):
    """
    Print the remaining HP of an entity.

    :param entity: a dict
    :param remaining_hp: an int
    :precondition: must be a properly formatted dictionary
    :post condition: will print the remaining hp of the provided entity
    :return: nothing

    """
    print(f"The hit left {entity['Alias']} with {remaining_hp}/{entity['HP'][1]} HP")
    return


def check_alive(character: dict) -> bool:
    """
    Check a character's health

    :param character: a dict
    :precondition: character must be a properly formed dictionary
    :post condition: will return a boolean based on the state of the character's life
    :return: a bool

    """
    if character['HP'][0] <= 0:
        return False
    else:
        return True


def startup():
    """
    Print the startup scenario.

    :return: nothing

    """
    print("You are awoken in a dark concrete room. Doors surround you on all sides.\n"
          "A trap door in the middle of the room protrudes the ceiling. It requires a key. \n"
          "You observe the empty room some more.\nWords scratched against the door - 'ESCAPE'.\n"
          "You realize that this is where you will come to get out of here. \n"
          "Find the key.")
    return


def get_user_choice_battle() -> bool:
    """
    Grab user input to determine if they want to run from or fight monster.

    :return: a boolean

    """
    user_input = bool(input("Would you like to fight[1] or run[0]?"))
    return user_input


def heal(health: int) -> int:
    """
    Heal the character by increasing their HP..

    :param health: an int
    :precondition: health must be an integer greater than 0
    :post condition: will return a character's updated HP
    :return: an int

    """
    if health < 9:
        health += 2
        print(f"Whilst moving around, you have healed a bit. You're now at {health}/10 HP ")
    elif health == 9:
        health += 1
        print(f"Whilst moving around, you have healed a bit. You're now at {health}/10 HP ")
    return health


def check_at_exit_with_key(position: dict, inventory: list) -> bool:
    """
    Determine if a character is at the exit coordinates with a key.

    :param position: a dict
    :param inventory: a list
    :precondition: position must be a dictionary containing valid coordinates
    :precondition: inventory must be a list
    :return: a boolean

    >>> check_at_exit_with_key({"x": 0, "y": 1}, [])
    False
    >>> check_at_exit_with_key({"x": 4, "y": 4}, ['key'])
    False
    >>> check_at_exit_with_key({"x": 2, "y": 2}, ['key'])
    True
    """
    if check_position(position, 2, 2) and inventory == ['key']:
        return True
    else:
        return False


def user_win():
    """
    Print a line to tell the user they won the game.

    :return: nothing

    """
    print("Greatest salutations young lad! You've escaped Kather's tunnels! You will make a noble warrior one day!")
    return


def fight_or_run() -> int:
    """
    Acquire user input to run or fight.

    :return: a bool

    """
    user_input = int(input("Would you like to fight [1] or run [0]?"))
    return user_input


def fight_monster(character: dict) -> list:
    """
    Ask user if they would like to fight or run from battle.

    Create a one in ten chance of getting damaged if character decides to run.
    :param character: a dict
    :precondition: character must be a properly formatted dictionary
    :post condition: will return character
    :return: a dict

    """
    user_decision = fight_or_run()
    if not user_decision:  # if character decides to run (inputs 0)
        if one_in_x_chance(10):  # will modify a character's HP with a one in ten chance
            damage = roll_die(1, 4)
            character['HP'][0] -= damage
            print(f"As you were running away, the monster swiped you and you lost {damage} HP!")
            print_remaining_hp(character, character['HP'][0])
        else:
            print("You ran away swiftly.......")
    return [user_decision, character]


def monster_encounter(character: dict) -> dict:
    """
    Determine the chance of a monster encounter, update the character after a battle if monster present.

    :param character: a dict
    :precondition: character must be a dictionary
    :post condition: will return an (non)updated dictionary
    :return: a dict

    """
    if one_in_x_chance(4):  # 1 in 4 chance to encounter monster
        monster = new_monster()
        user_decision = fight_monster(character)
        if user_decision[0]:  # if user decides to fight, simulate battle and return result
            return battle(character, monster)
        else:
            return user_decision[1]  # if user decides to run, return the updated character information
    else:
        return character  # return character if no monster is encountered


def run_game():
    """
    Run the SUD.

    The main flow of the game that calls all functions.
    :return: nothing

    """
    character = create_character()  # creates a new character
    startup()  # print the starting scenario
    while True:
        print_position(character["position"])  # show the current position of character
        direction = get_move()  # assigns user input to direction
        valid_move = validate_move(character['position'], direction)  # validates a move based on position and direction
        if direction == 'quit':  # break the loop when user inputs quit
            print('K bye.')  # K bye.
            break
        elif valid_move:  # move the character and encounter monster if user input is valid
            character["position"] = move_character(character["position"], direction)  # update user position when moving
            character["HP"][0] = heal(character["HP"][0])  # heal the character each time they move
            if check_at_exit_with_key(character['position'], character['Inventory']):  # will break loop if user escapes
                user_win()
                break
            character = monster_encounter(character)  # check if monster present, update info based on actions performed
            if not check_alive(character):  # break the loop if character is not alive
                print("You died. Please try again.")
                break
        else:  # print something when input is not recognized and/or invalid
            print("Not a valid move. Try moving in another direction.")


if __name__ == "__main__":
    doctest.testmod()
    run_game()

