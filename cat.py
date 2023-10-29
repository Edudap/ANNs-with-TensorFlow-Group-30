class Cat:
    def __init__(self, name):
        self.name = name

    def greet(self, other_cat):
        print(f"Hello I am {self.name}! I see you are also a cool jungle rascal {other_cat.name}, "
              f"let's meow like crazy and not let anyone sleep")