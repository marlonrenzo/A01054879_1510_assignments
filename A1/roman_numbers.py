# def convert_to_roman_numeral(user_input):
#     """
#     Convert positive integer into a roman numeral string.
#
#     :param user_input: positive integer to convert
#     :precondition: number must be a postive integer between 1 an 10,000
#     :postcondition: converts to a roman numeral
#     :return: a roman numeral as a string
#     """
#     numerals_ones = ("","I","II","III","IV","V","VI","VII","VIII","IX")
#     numerals_tens = ("","X","XX","XXX","XL","L","LX","LXX","LXXX","XC")
#     numerals_hundreds = ("","C","CC","CCC","CD","D","DC","DCC","DCCC","CM")
#     numerals_thousands = ("","M","MM","MMM","MMMM","MMMMM","MMMMMM","MMMMMMM","MMMMMMMM","MMMMMMMMM")
#     numerals_ten_thousand = "MMMMMMMMMM"
#
#     # user_input = int(input("Enter a number between 1 - 10,000:\n"))
#     string_user_input = str(user_input)
#     length = len(string_user_input)
#
#     if length == 1:
#         return numerals_ones[user_input]
#     elif length == 2:
#         string_user_one = int(string_user_input[0])
#         string_user_two = int(string_user_input[1])
#         roman_numeral = numerals_tens[string_user_one] + numerals_ones[string_user_two]
#         return roman_numeral
#     elif length == 3:
#         string_user_one = int(string_user_input[0])
#         string_user_two = int(string_user_input[1])
#         string_user_three = int(string_user_input[2])
#         roman_numeral = numerals_hundreds[string_user_one] + numerals_tens[string_user_two] + numerals_ones[string_user_three]
#         return roman_numeral
#     elif length == 4:
#         string_user_one = int(string_user_input[0])
#         string_user_two = int(string_user_input[1])
#         string_user_three = int(string_user_input[2])
#         string_user_four = int(string_user_input[3])
#         roman_numeral = numerals_thousands[string_user_one] + numerals_hundreds[string_user_two] + numerals_tens[string_user_three] + numerals_ones[string_user_four]
#         return roman_numeral
#     elif length == 5:
#         roman_numeral = numerals_ten_thousand
#         return roman_numeral
#     else:
#         return None

import doctest


def convert_to_roman_numeral(user_input):
    """
    Call all necessary fucntions to correctly represent an integer as a roman numeral.

    :precondition: must be a positive integer
    :precondition: must be in the range [1, 10_000]
    :param user_input: The integer to be converted
    :return: The corresponding roman numeral as a string
    >>> convert_to_roman_numeral(0)
    ''
    >>> convert_to_roman_numeral(10)
    'X'
    >>> convert_to_roman_numeral(9999)
    'MMMMMMMMMCMXCIX'
    """
    thousands = find_thousands(user_input)
    thousands_letters = get_letters(thousands, "M")
    remainder = find_remainder(user_input, thousands, 1000)

    hundreds = find_hundreds(remainder)
    hundreds_letters = get_letters(hundreds, "C")
    remainder_hundreds = find_remainder(remainder, hundreds, 100)

    tens = find_tens(remainder_hundreds)
    tens_letters = get_letters(tens, "X")
    remainder_tens = find_remainder(remainder_hundreds, tens, 10)

    fives = find_fives(remainder_tens)
    fives_letters = get_letters(fives, "V")
    remainder_fives = find_remainder(remainder_tens, fives, 5)

    ones = find_ones(remainder_fives)
    ones_letters = get_letters(ones, "I")

    roman_numeral = final_conversion(thousands_letters, hundreds_letters, tens_letters, fives_letters, ones_letters)
    return roman_numeral



def get_letters(place_value, roman_numeral_string):
    """
    Convert a place value with the associated roman numeral string into the correct string of characters to represent the value.

    :precondition: roman_numeral must be a string
    :precondition: must be a postive integer
    :postcondition: returns a value that will make up part of the final string
    :param place_value: The value found in a particular number place as an int
    :param roman_numeral_string: The character associated witht the place value as as string
    :return: The correct string of characters to represent the place value as a string
    >>> get_letters(1, "a")
    'a'
    >>> get_letters(4, "X")
    'XL'
    >>> get_letters(15, "x")
    'xxxxxxxxxxxxxxx'
    >>> get_letters(10, "I")
    'X'
    """
    if place_value == 4 or place_value == 9:
        string = replace_4_or_9(place_value, roman_numeral_string)
        return string

    if place_value == 5 or place_value == 10:
        string = replace_5_or_10(place_value, roman_numeral_string)
        return string

    elif place_value == 0:
        return ""

    else:
        string = roman_numeral_string * place_value
        return string


def replace_4_or_9(value, roman_numeral_string):
    """
    Replace a string with the value 4 or 9 into a fifth or tenth character.

    :precondition: value must be a positive integer
    :precondition: roman_numeral_string must be a string
    :precondition: value must equal 4 or 9
    :postcondition: will return the correct string of characters for the corresponding value
    :param value: The value found in a particular number place as an int
    :param roman_numeral_string: The character associated with the place value as a string
    :return: The correct string for the corresponding place value
    >>> replace_4_or_9(4, "X")
    'XL'
    >>> replace_4_or_9(9, "C")
    'CM'
    >>> replace_4_or_9(4, "test")

    """
    if value == 4:
        if roman_numeral_string == "C":
            return "CD"
        if roman_numeral_string == "I":
            return "IV"
        if roman_numeral_string == "X":
            return "XL"
        if roman_numeral_string == "M":
            return "MMMM"
    if value == 9:
        if roman_numeral_string == "C":
            return "CM"
        if roman_numeral_string == "I":
            return "IX"
        if roman_numeral_string == "X":
            return "XC"
        if roman_numeral_string == "M":
            return "MMMMMMMMM"


def replace_5_or_10(value, roman_numeral_string):
    """
    Replace a string with the value 5 or 10 into a fifth or tenth character.

    :precondition: value must be a positive integer
    :precondition: roman_numeral_string must be a string
    :precondition: value must equal 5 or 10
    :param value: The value found in a particular number place as an int
    :param roman_numeral_string: The character associated with the place value as a string
    :return: The correct string for the corresponding place value
    >>> replace_5_or_10(5, "X")
    'L'
    >>> replace_5_or_10(10, "C")
    'D'
    >>> replace_5_or_10(5, "test")

    """
    if value == 5:
        if roman_numeral_string == "C":
            return "D"
        if roman_numeral_string == "I":
            return "V"
        if roman_numeral_string == "X":
            return "L"
        if roman_numeral_string == "M":
            return "MMMMM"
    if value == 10:
        if roman_numeral_string == "C":
            return "D"
        if roman_numeral_string == "I":
            return "X"
        if roman_numeral_string == "X":
            return "C"
        if roman_numeral_string == "M":
            return "MMMMMMMMMM"


def find_remainder(original_value, converted_value, multiplier):
    """
    Determine the remainder of a number after it gets subracted by converted value in a number's place and multuplier.

    The converted value is multiplied by the multiplier that will equal the place value.

    :precondition: original value must be a positive integer
    :postcondition: will return a positive integer
    :param original_value: the value left for the next place value as an int
    :param converted_value: the value found in the place value as an int
    :param multiplier: the place value as an int
    :return: the excess value after subtracting the amount found in the place value as an int
    >>> find_remainder(1, 1, 0)
    1
    >>> find_remainder(100000, 5, 100)
    99500
    >>> find_remainder(785, 7, 5)
    750
    """
    excess_value = original_value - (converted_value * multiplier)
    excess_value = int(excess_value)
    return excess_value


def find_thousands(number):
    """
    Convert a number to a place value in the thousands place.

    :precondition: must be a positive integer
    :postcondition: will return a value for the thousands place value
    :param number: the value to convert as an int
    :return: thousands place value as an int
    >>> find_thousands(1000000)
    1000
    >>> find_thousands(999)
    0
    >>> find_thousands(2000)
    2
    """
    if number == 10000:
        return 10
    elif number >= 1000:
        number = int(number / 1000)
        return number
    elif number < 1000:
        return 0


def find_hundreds(number):
    """
    Convert a number to a place value in the hundreds place.

    :precondition: must be a positive integer
    :postcondition: will return a value for the hundreds place value
    :param number: the value to convert as an int
    :return: hundreds place value
    >>> find_hundreds(10000)
    100
    >>> find_hundreds(100)
    1
    >>> find_hundreds(99)
    0
    """
    if number >= 100:
        number = int(number / 100)
        return number
    elif number < 100:
        return 0



def find_tens(number):
    """
    Convert a number to a place value in the tens place.

    :precondition: must be a positive integer
    :postcondition: will return a value for the tens place value
    :param number: the value to convert as an int
    :return: tens place value
    >>> find_tens(10090)
    1009
    >>> find_tens(9)
    0
    >>> find_tens(99)
    9
    """
    if number >= 10:
        number = int(number / 10)
        return number
    elif number < 10:
        return 0

def find_fives(number):
    """
    Convert a number to a place value in the fives place.

    Check if the value is nine, if the value isn't nine return the number to prevent errors in the conversion process.

    If the value is 9, then return a value that will represent the number of fives in the remainder.
    :precondition: must be a positive integer
    :postcondition: will return a value for the fives place value
    :param number: the value to convert as an int
    :return: fives place value
    >>> find_fives(560)
    112
    >>> find_fives(5)
    1
    >>> find_fives(9)
    0
    """
    if number !=9:
        number = int(number / 5)
        return number
    elif number < 10:
        return 0
    else:
        return number


def find_ones(number):
    """
    Convert a number to a place value in the ones place.

    :precondition: must be a positive integer
    :postcondition: will return a value for the ones place value
    :param number: the value to convert as an int
    :return: ones place value
    >>> find_ones(560)
    560
    >>> find_ones(5)
    5
    >>> find_ones(0)
    0
    """
    number = int(number / 1)
    return number


def final_conversion(thousands, hundreds, tens, fives, ones):
    """
    Format the final place value letters into one concatenated string.

    :precondition: all parameters must be string
    :postcondition: will return a concatenated string
    :param thousands: letters in the thousands place as a string
    :param five_hundreds: letters in the five hundreds place
    :param hundreds: letters in the hundreds place as a string
    :param fifties: letters in the fifties place
    :param tens: letters in the tens place as a string
    :param fives: letters in the fives place as a string
    :param ones: letters in the ones place as a string
    :return: a concatenated string
    >>> final_conversion("","","test   ","test","test")
    'testtesttest'
    >>> final_conversion("one","two","  three  ","four","five")
    'onetwothreefourfive'
    >>> final_conversion("","","","","")
    ''
    """
    format = thousands.strip() + hundreds.strip() + tens.strip() + fives.strip() + ones.strip()
    return format


def main():
    """Run the program by calling the main function."""
    print(convert_to_roman_numeral(4999))
    print(convert_to_roman_numeral(498))
    print(convert_to_roman_numeral(54))
    doctest.testmod()


if __name__ == '__main__':
    main()