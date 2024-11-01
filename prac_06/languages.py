"""
Time to completion EST: 2 hours
Actual Time to Completion: 1 hour
"""


from programming_language import ProgrammingLanguage


def main():
    """Demonstrate the usage of the ProgrammingLanguage class."""

    # Create ProgrammingLanguage objects with various attributes
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print the string representation of the Python object
    # This calls the __str__ method defined in the ProgrammingLanguage class
    print(python)

    # Create a list to store the language objects
    languages = [python, ruby, visual_basic]

    # Print the names of dynamically typed languages
    print("The dynamically typed languages are:")
    for language in languages:
        # Use the is_dynamic method to check for dynamic typing
        if language.is_dynamic():
            # Print the name of the language if it is dynamically typed
            print(language.name)

# Run the main function when the script is executed directly
if __name__ == "__main__":
    main()