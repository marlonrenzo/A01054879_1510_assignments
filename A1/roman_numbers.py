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




def convert_to_roman_numeral(user_input):
    """

    :return:
    """
    thousands = find_thousands(user_input)
    thousands_letters = get_letters(thousands, "M")
    remainder = find_remainder(user_input, thousands, 1000)

    hundreds = find_hundreds(remainder)
    hundreds_letters = get_letters(hundreds, "C")
    remainder_hundreds = find_remainder(remainder, hundreds, 100)

    tens = find_tens(remainder_hundreds)
    tens_letters = get_letters(tens, "X")
    remainder_tens = find_remainder(remainder_hundreds, tens, 100)

    ones = find_ones(user_input)
    ones_letters = get_letters(ones, "I")
    final_conversion
    return final_conversion


def get_letters(place_value, roman_numeral_string):

    if place_value == 4 or 9:
        string = replace_4_or_9(place_value, roman_numeral_string)
        return string
    if place_value == 5 or 10:
        string = replace_5_or_10(place_value, roman_numeral_string)
        return string
    elif place_value != 4 or 9 or 5 or 10:
        string = roman_numeral_string * place_value
        return string
    elif place_value == 0:
        return place_value


def replace_4_or_9(length, roman_numeral_string):
    if length == 4:
        if roman_numeral_string == "C":
            return "CD"
        if roman_numeral_string == "I":
            return "IV"
        if roman_numeral_string == "X":
            return "XL"
        if roman_numeral_string == "C":
            return "CD"
    if length == 9:
        if roman_numeral_string == "C":
            return "CD"
        if roman_numeral_string == "I":
            return "IV"
        if roman_numeral_string == "X":
            return "XL"
        if roman_numeral_string == "C":
            return "CD"


def replace_5_or_10(length, roman_numeral_string):
    if length == 5:
        if roman_numeral_string == "C":
            return "D"
        if roman_numeral_string == "I":
            return "V"
        if roman_numeral_string == "X":
            return "L"
        if roman_numeral_string == "M":
            return "MMMMM"
    if length == 10:
        if roman_numeral_string == "C":
            return "CD"
        if roman_numeral_string == "I":
            return "IV"
        if roman_numeral_string == "X":
            return "XL"
        if roman_numeral_string == "M":
            return "MMMMMMMMMM"


def find_remainder(original_value, converted_value, multiplier):
    """

    :param original_value:
    :param subtracting_value:
    :return:
    """
    excess_value = original_value - (converted_value * multiplier)
    excess_value = int(excess_value)
    return excess_value


def find_thousands(number):
    if number == 10000:
        return 10
    elif number >= 1000:
        number = int(number / 1000)
        return number
    elif number < 1000:
        return 0


def find_hundreds(number):
    if number >= 100:
        number = int(number / 100)
        return number
    elif number < 100:
        return 0

def find_tens(number):
    if number >= 10:
        number = int(number / 10)
        return number
    elif number < 10:
        return 0

def find_ones(number):
    number = int(number / 10)
    return number














def main():
    # print(convert_to_roman_numeral(14))
    # print(convert_to_roman_numeral(84))
    print(convert_to_roman_numeral(400))
    # test = 4
    # print(replace_4_or_9(test,"I"))


    # user_input = 400
    # thousands = find_thousands(user_input)
    # thousands_letters = get_letters(thousands, "M")
    # remainder = find_remainder(user_input, thousands, 1000)
    # hundreds = find_hundreds(remainder)
    # print(hundreds)


    # hundreds_letters = get_letters(hundreds, "C")
    # remainder_hundreds = (remainder, hundreds, 100)
    # print(find_hundreds(hundres_letters))







if __name__ == '__main__':
    main()