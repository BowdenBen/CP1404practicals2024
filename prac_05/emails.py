"""
Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
Ask the user for their email until they enter a blank one.
By Benjamin Bowden
Estimate: 30 minutes
Actual:    minutes
"""


def extract_name_from_email(email):
    # Split the email at '@' to get the local part (before the '@')
    local_part = email.split('@')[0]

    # Split the local part at '.' or '_' to get individual parts of the name
    # This will handle names like "john.doe" or "john_doe"
    if '.' in local_part:
        name_parts = local_part.split('.')
    else:
        name_parts = local_part.split('_')

    # Capitalize each part of the name using title() and join them with spaces
    name = ' '.join(part.title() for part in name_parts)

    return name


def main:

    email_to_name = {}

    email = "placeholder"

    While email != "":
        # Prompt the user to enter their email
        email = input("Email: ")

        Call extract_name_from_email(email) to get a suggested name.
        Prompt the user: "Is your name [suggested_name]? (Y/n)".

        If the user enters "Y" or presses "Enter":
            Set name = suggested_name.
        Else:
            Prompt the user to enter their actual name: "Name: ".
            Set name = entered name.

        Store the email (as key) and name (as value) in the dictionary.

    End of loop.

    For each email-name pair in email_to_name:
        Print the name and email in the format: "Name (email)".
