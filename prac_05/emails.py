"""
Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
Ask the user for their email until they enter a blank one.
By Benjamin Bowden
Estimate: 30 minutes
Actual:    minutes
"""

Function extract_name_from_email(email):
    Split the email at '@' to separate the local part from the domain.
    Split the local part again at "." or "_" to extract individual parts of the name.
    Capitalize each part of the name using title().
    Join the parts back together with spaces.
    Return the formatted name.

Main function:
    Initialize an empty dictionary: email_to_name.

    While True:
        Prompt the user to enter their email: "Email: "
        If the email is blank, break the loop.

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
