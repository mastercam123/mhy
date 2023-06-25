class Animal:
    def __init__(self, type, color, dietary):
        self.type = type
        self.color = color
        self.dietary = dietary

    def colour(self):
        print("My skin is " + self.color)

    def eating(self):
        print("I eat as a " + self.dietary)


