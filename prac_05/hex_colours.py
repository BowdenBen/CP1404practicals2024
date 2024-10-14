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

# Start an infinite loop
loop:
# Prompt the user to enter a color name
color_name = get
user
input("Enter color name (or blank to quit)")

# Remove leading/trailing spaces and convert to lowercase
color_name = trim
spaces and convert
to
lowercase

# If the input is blank, break the loop
if color_name is blank:
    break
    the
    loop

# Check if color name exists in the dictionary
if color_name exists in COLORS:
    # Display the hex code for the color
    print
    "The hex code for color_name is COLORS[color_name]"
else:
    # Print error message for invalid color name
    print
    "Sorry, that color is not found"

# End of the program
