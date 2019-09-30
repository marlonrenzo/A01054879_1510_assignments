import random


def rock_paper_scissors():
    """

    :return:
    """
    input = input("Choose Rock, Paper, or Scissors")

    input = check_win(input)
    return input


def check_win(input):
    """

    :param input:
    :return:
    """
    input = format_input(input)
    computer_choice = random_choice()
    string = input + computer_choice()
    win_or_lose = print_win_or_loss(string)
    return win_or_lose


def print_win_or_lose(string):
    """
    Return a string saying if the user beat the computer.

    :param string:
    :return:
    """
    string = string.replace("rockrock", "It is a draw, try again")
    string = string.replace("rockscissors", "You won! Congrats!")
    string = string.replace("rockpaper", "You lost, please try again.")
    string = string.replace("paperpaper", "It is a draw, try again")
    string = string.replace("paperscissors", "You lost, please try again")
    string = string.replace("paperrock", "You won! Congrats!")
    string = string.replace("scissorsscissors", "It is a draw, try again")
    string = string.replace("scissorspaper", "You won! Congrats!")
    string = string.replace("scissorsrock", "You lost, please try again.")

    return string


def computer_choice():
    random_choice = random.randint(1,3)
    if random_choice == 1:
        return "rock"
    if random_choice == 2:
        return "paper"
    if random_choice == 3:
        return "scissors"


def format_input(string):
    """
    Format a string to match the same look.

    :precondition: parameter must be a string
    :postcondition: will return a formatted string
    :param string: the string to be formatted
    :return: a stripped and lowercased string
    >>> format_input("  ASdfGhJkl  ")
    'asdfghjkl'
    >>> format_input("QWERTY")
    'qwerty'
    >>> format_input("      BlUe")
    'blue'
    """
    string = string.lower()
    string = string.strip()

    return string


def main():
    """Run the program by calling the main function."""
    print(rock_paper_scissors())





if __name__ == '__main__':
    main()