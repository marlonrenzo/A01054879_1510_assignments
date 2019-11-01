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


def move(position, direction):
    action = {"up": 1, "down": -1, "left": -1, "right": 1}
    if direction == "up" or direction == "down":
        position["x-pos"] += action[direction]
    elif direction == "right" or direction == "left":
        position["y-pos"] += action[direction]
    return position


def print_position(position):
    position_holder = ["[ ]", "[x]"]
    for y_axis in range(4, -1, -1):
        print("\n")
        for x_axis in range(5):
            print(position_holder[check_position(position, x_axis, y_axis)], end="")


def check_position(position, x_position, y_position):
    if position["x-pos"] == x_position and position["y-pos"] == y_position:
        return 1
    else:
        return 0


def main():
    position = {"x-pos": 0, "y-pos": 0}
    while True:
        user_input = input("\nWhat do you want to do?")
        if user_input.lower() == "quit":
            print("Thanks for playing!")
            break
        elif user_input.lower() == "position":
            print_position(position)
        else:
            position = move(position, user_input)
            print_position(position)


if __name__ == "__main__":
    main()
