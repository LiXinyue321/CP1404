class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns True/False if the programming language is dynamically typed or not"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of a programming language"""
        return f"{self.name}, {self.typing} typing, {self.reflection}, First appeared in {self.year}"