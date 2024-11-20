from person import Person


class Musician(Person):
    def __init__(self, style: str, play: int, **kwargs):
        super().__init__(**kwargs)
        self.style = style
        self.play = play

    def __repr__(self):
        return f"Musician: {self.name}, Age: {self.age()}, Style: {self.style}, Time played: {self.play} hours"