class ProgrammingLanguage:
    """Represent a programming language with specific attributes."""

    def __init__(self, name, typing, reflection, year):
        """
        Initialize a ProgrammingLanguage instance.

        param name: str, name of the programming language
        param typing: str, type of typing (e.g., "Static" or "Dynamic")
        param reflection: bool, whether the language supports reflection
        param year: int, year the language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """
        Determine if the language uses dynamic typing.
        return: True if the language has dynamic typing, otherwise False
        """
        return self.typing == "Dynamic"

    def __str__(self):
        """
        Provide a string representation of the ProgrammingLanguage instance.
        return: str, formatted description of the language
        """
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
