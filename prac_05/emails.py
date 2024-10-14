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


def main():

    email_to_name = {}

    email = "placeholder"

    # Continue asking for input until the user enters an empty email
    while email != "":
        # Prompt the user to enter their email
        email = input("Email: ")

        # Only proceed if the email is not empty
        if email != "":
            # Extract a suggested name from the email
            suggested_name = extract_name_from_email(email)

            # Ask the user to confirm if the extracted name is correct
            confirmation = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()

            if confirmation == "" or confirmation == "y":
                # If the user presses Enter or 'Y', use the suggested name
                name = suggested_name
            else:
                # Otherwise, ask for the user's actual name
                name = input("Name: ")

            # Store the email (as key) and name (as value) in the dictionary
            email_to_name[email] = name

    # After exiting the loop, print the names and emails in the specified format
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

# Run the main function
if __name__ == "__main__":
    main()