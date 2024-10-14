# Define a constant dictionary of color names and hex codes
COLORS = {hexadecimal colour codes}

# Start an infinite loop
loop:
    # Prompt the user to enter a color name
    color_name = get user input ("Enter color name (or blank to quit)")

    # Remove leading/trailing spaces and convert to lowercase
    color_name = trim spaces and convert to lowercase

    # If the input is blank, break the loop
    if color_name is blank:
        break the loop

    # Check if color name exists in the dictionary
    if color_name exists in COLORS:
        # Display the hex code for the color
        print "The hex code for color_name is COLORS[color_name]"
    else:
        # Print error message for invalid color name
        print "Sorry, that color is not found"

# End of the program
