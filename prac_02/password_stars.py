

def main():
    min_length = 8

    password = check_password(min_length)

    print_asterix(password)


def print_asterix(password):
    print(" * " * len(password))


def check_password(min_length):
    password = input("Enter a password: ")
    while len(password) < min_length:
        print("Password must be at lease {} characters long.".format(min_length))
        password = input("Enter a password: ")
    return password


main()