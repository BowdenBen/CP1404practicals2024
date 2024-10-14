"""
Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
Ask the user for their email until they enter a blank one.
By Benjamin Bowden
Estimate: 30 minutes
Actual:  45  minutes
"""

def extract_name_from_email(email):
    """
    Extracts and formats a name from an email address.
    Example: "john.doe@example.com" -> "John Doe"
    """
    # Split the email at '@' to get the local part (before the '@')
    local_part = email.split('@')[0]

    # Split the local part at '.' or '_' to get individual parts of the name
    # This handles names like "john.doe" or "john_doe"
    if '.' in local_part:
        name_parts = local_part.split('.')
    else:
        name_parts = local_part.split('_')

    # Capitalize each part of the name using title() and join them with spaces
    name = ' '.join(part.title() for part in name_parts)

    # Return the formatted name
    return name


def main():
    """
    Main function to prompt the user for emails and store names based on them.
    Users can confirm or edit their name before it is saved.
    """
    # Initialize an empty dictionary to store emails (keys) and names (values)
    email_to_name = {}

    # Initialize email with a placeholder string to enter the loop
    email = "placeholder"

    # Continue asking for input until the user enters an empty email
    while email != "":
        # Prompt the user to enter their email
        email = input("Email: ")

        # Only proceed if the email is not empty (the user has not pressed Enter to finish)
        if email != "":
            # Extract a suggested name from the email by calling extract_name_from_email function
            suggested_name = extract_name_from_email(email)

            # Ask the user to confirm if the extracted name is correct
            confirmation = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()

            # If the user presses Enter or inputs 'Y' (case-insensitive), accept the suggested name
            if confirmation == "" or confirmation == "y":
                name = suggested_name
            else:
                # Otherwise, ask for the user's actual name
                name = input("Name: ")

            # Store the email as the key and the name as the value in the dictionary
            email_to_name[email] = name

    # After exiting the loop (when the user enters an empty email), print the stored names and emails
    for email, name in email_to_name.items():
        # Format and print each name and email in the specified format: "Name (email)"
        print(f"{name} ({email})")


# Run the main function only if the script is executed directly
if __name__ == "__main__":
    main()
