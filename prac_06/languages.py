from programming_language import ProgrammingLanguage


def main():
    # Create language objects
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# # Print the string representation of Python
# Print python
#
# # Create a list of languages
# languages = [python, ruby, visual_basic]
#
# Print "The dynamically typed languages are:"
#
# # Loop through the languages list
# For language in languages:
#     If language.is_dynamic():
#         Print language.name
if __name__ == "__main__":
    main()