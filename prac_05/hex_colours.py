"""
Use a constant dictionary of about 10 colour names
and write a program that allows a user to enter a name and get the code

By Benjamin Bowden
"""

# Define a constant dictionary with 10 color names and their hex codes
COLOURS = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aqua": "#00ffff", "aquamarine": "#7fffd4",
          "azure": "#f0ffff", "beige": "#f5f5dc", "bisque": "#ffe4c4", "black": "#000000",
          "blanchedalmond": "#ffebcd", "blue": "#0000ff"}
for name, colour in COLOURS.items():
    print(f"{name:16}{colour}")


# Input and process colour using EAFP
code_colour = input("Enter colour from list: ").lower()
while code_colour != "":
    try:
        # If the colour exists in COLOURS, this will succeed, and the colour's code is printed.
        print(f"The HEX code for {code_colour} is {COLOURS[code_colour]}.")
    except KeyError:
        # If the colour doesn't exist in the dictionary, a KeyError is raised.
        # The KeyError is caught and an error message is displayed to the user.
        print("Sorry, that color is not found")
    # After processing, ask the user for another colour.
    # The input is again converted to uppercase to maintain case-insensitivity.
    code_colour = input("Enter colour from list: ").lower()
