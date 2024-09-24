min_length = 8

password = input("Enter a password: ")

while len(password) < min_length:
    print("Password must be at lease {} characters long.".format(min_length))
    password = input("Enter a password: ")

print(" * " * len(password))