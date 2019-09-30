import random
import doctest

def rock_paper_scissors():
    """
    Run the program by getting a user input and calling necessary functions.

    :return: a string based on the output
    """
    user_input = input("Choose Rock, Paper, or Scissors:\n")

    user_input = check_win(user_input)
    return user_input


def check_win(input):
    """
    Determine the outcome of the game.

    :precondition: the parameter must be rock, paper or scissors as a string
    :postcondition: will return the outcome of the game as a string
    :param input: the user input as a string
    :return: a string
    >>> check_win("string")
    "Your entry is not valid, ensure you're inputting only rock, paper or scissors."
    """
    input = format_input(input)
    computer_choice = random_choice()

    valid_choice = check_input(input)

    if valid_choice == True:
        string = input + computer_choice
        win_or_lose = print_win_or_loss(string)
        return win_or_lose

    else:
        return valid_choice

def check_input(string):
    """
    Check to see if the string is a valid input.

    :precondition: must be a string
    :postcondition: will return the validity
    :param string: a string to be checked
    :return: will determine the validity of the string
    >>> check_input("scissors")
    True
    >>> check_input("rockkk")
    "Your entry is not valid, ensure you're inputting only rock, paper or scissors."
    >>> check_input("papeer")
    "Your entry is not valid, ensure you're inputting only rock, paper or scissors."
    >>> check_input("rock")
    True
    """
    if string == "rock" or string ==  "paper" or string ==  "scissors":
        return True
    else:
        return "Your entry is not valid, ensure you're inputting only rock, paper or scissors."


def print_win_or_loss(string):
    """
    Return a string saying if the user beat the computer.

    :precondition: the string must be rock, paper, or scissors
    :postcondition: will return a string determining the outcome of the game
    :param string: a valid combination of the user input and user choice
    :return: a string based on the corresponding replacement
    >>> print_win_or_loss("paperpaper")
    'It is a draw, try again'
    >>> print_win_or_loss("rockkkkrock")
    'rockkkkrock'
    >>> print_win_or_loss("scissorsrock")
    'You lost, please try again.'
    """
    string = string.replace("rockrock", "It is a draw, try again.")
    string = string.replace("rockscissors", "You won! Congrats!")
    string = string.replace("rockpaper", "You lost, please try again.")
    string = string.replace("paperpaper", "It is a draw, try again")
    string = string.replace("paperscissors", "You lost, please try again")
    string = string.replace("paperrock", "You won! Congrats!")
    string = string.replace("scissorsscissors", "It is a draw, try again")
    string = string.replace("scissorspaper", "You won! Congrats!")
    string = string.replace("scissorsrock", "You lost, please try again.")

    return string


def random_choice():
    """
    Produce a random choice by theRO computer.

    :return: a choice by the computer as an int
    """
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
    >>> format_input("    STRING    ")
    'string'
    >>> format_input(" sTrInG   ")
    'string'
    >>> format_input(" s T r I n g ")
    's t r i n g'
    """
    string = string.lower()
    string = string.strip()

    return string


def main():
    """Run the program by calling the main function."""
    print(rock_paper_scissors())
    doctest.testmod()




if __name__ == '__main__':
    main()