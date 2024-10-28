class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
#
#     Method is_dynamic():
#         If self.typing equals "Dynamic":
#             Return True
#         Else:
#             Return False
#
#     Method __str__():
#         Return formatted string with name, typing, reflection, and year
