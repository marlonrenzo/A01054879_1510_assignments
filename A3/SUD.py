from A3.character import create_character


def move(position):
    """
    Change the position of a character based on direction.

    Use the direction inputted by the user to change the dictionary accordingly.
    :param position: a dictionary
    :precondition: position must be a dictionary
    :post condition: will return an updated dictionary
    :return: a dictionary
    """
    action = {"up": -1, "down": 1, "left": -1, "right": 1}
    direction = input("What direction would you like to move? (up, down left or right)")
    if (direction.lower() == "up" or direction.lower() == "down") and position["y-pos"] < 5:
        position["y-pos"] += action[direction]
    elif (direction.lower() == "right" or direction.lower() == "left") and position["y-pos"] < 5:
        position["x-pos"] += action[direction]
    else:
        print("Invalid entry, please only move 'up', 'down', 'left', or 'right'")
    print_position(position)
    return position


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
    if position["x-pos"] == x_position and position["y-pos"] == y_position:
        return 1
    else:
        return 0


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
        actions = {0: ["Move", move], 1: ["Show position", print_position], 2: ["Quit"]}
        for x in actions.keys():
            print(f"{x}: {actions[x][0]}")
        user_action = int(input("\nWhat would you like to do?"))
        if 0 <= user_action <= 1:
            actions[user_action][1](character["position"])
        elif user_action == 2:
            print("Thanks for playing!")
            break
        else:
            print("That was not a valid entry. Please try again.")


if __name__ == "__main__":
    run_game()
