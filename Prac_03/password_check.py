MIN_LENGTH = 5


def main():


    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    password = input("Enter a password with at least {} characters: ".format(minimum_length))
    while len(password) < MIN_LENGTH:
        print("Password length must be {} or more characters.".format(minimum_length))
        password = input("Enter a password with at least {} characters: ".format(minimum_length))
    return password


def print_asterisks(password_length):
    print("*" * len(password_length))


main()