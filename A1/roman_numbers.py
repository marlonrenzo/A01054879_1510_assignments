def convert_to_roman_numeral(user_input):
    """
    Convert positive integer into a roman numeral string.

    :param user_input: positive integer to convert
    :precondition: number must be a postive integer between 1 and 10,000
    :postcondition: converts to a roman numeral
    :return: a roman numeral as a string
    """
    numerals_ones = ("","I","II","III","IV","V","VI","VII","VIII","IX")
    numerals_tens = ("","X","XX","XXX","XL","L","LX","LXX","LXXX","XC")
    numerals_hundreds = ("","C","CC","CCC","CD","D","DC","DCC","DCCC","CM")
    numerals_thousands = ("","M","MM","MMM","MMMM","MMMMM","MMMMMM","MMMMMMM","MMMMMMMM","MMMMMMMMM")
    numerals_ten_thousand = "MMMMMMMMMM"

    # user_input = int(input("Enter a number between 1 - 10,000:\n"))
    string_user_input = str(user_input)
    length = len(string_user_input)

    if length == 1:
        return numerals_ones[user_input]
    elif length == 2:
        string_user_one = int(string_user_input[0])
        string_user_two = int(string_user_input[1])
        roman_numeral = numerals_tens[string_user_one] + numerals_ones[string_user_two]
        return roman_numeral
    elif length == 3:
        string_user_one = int(string_user_input[0])
        string_user_two = int(string_user_input[1])
        string_user_three = int(string_user_input[2])
        roman_numeral = numerals_hundreds[string_user_one] + numerals_tens[string_user_two] + numerals_ones[string_user_three]
        return roman_numeral
    elif length == 4:
        string_user_one = int(string_user_input[0])
        string_user_two = int(string_user_input[1])
        string_user_three = int(string_user_input[2])
        string_user_four = int(string_user_input[3])
        roman_numeral = numerals_thousands[string_user_one] + numerals_hundreds[string_user_two] + numerals_tens[string_user_three] + numerals_ones[string_user_four]
        return roman_numeral
    elif length == 5:
        roman_numeral = numerals_ten_thousand
        return roman_numeral
    else:
        return None


def main():
    print(convert_to_roman_numeral(14))
    print(convert_to_roman_numeral(84))
    print(convert_to_roman_numeral(999))






if __name__ == '__main__':
    main()