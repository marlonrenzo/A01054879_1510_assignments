import doctest

def colour_mixer():
    input_one = input("Enter a primary colour here:\n")
    input_two = input("Enter a second primary colour here:\n")
    input_one = input_one.lower()
    input_one = input_one.strip()
    input_two = input_two.lower()
    input_two = input_two.strip()

    string = input_one + input_two

    string = string.replace("bluered", "Purple")
    string = string.replace("redblue", "Purple")
    string = string.replace("yellowblue", "Green")
    string = string.replace("blueyellow", "Green")
    string = string.replace("redyellow", "Orange")
    string = string.replace("redyellow", "Orange")

    return string






def main():
    """Run the program by calling the main function."""
    print(colour_mixer())




if __name__ == '__main__':
    main()