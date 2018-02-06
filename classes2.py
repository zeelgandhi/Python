class Animal():
    name = "Amy"
    noise = "Grunt"
    size = "Large"
    colour = "Brown"
    hair = "Covers body"

    def get_colour(self, abc):
        return self.colour + " " + abc
    @property
    def make_noise(self):
        return self.noise

dog = Animal()
print(dog.get_colour("green"))
print(dog.make_noise)
    
