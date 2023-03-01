class Dog:
    def __init__(self, name, age, colour, danger):  # the self parameter
        # (e.g. dog1 or dog2) is automatically passed to the dog class
        # - so that we know which dog we're talking about

        self.name = name  # Creates a 'name' attribute for Dog
        self.age = age  # Creates a 'age' attribute for Dog
        self.colour = colour  # Creates a 'colour' attribute for Dog
        self.danger = danger  # Creates a 'danger' attribute for Dog

    def print_details(self):  # Creates a method of displaying information
        return f"{self.name} is a {self.danger} {self.colour} dog and is {self.age}."

    def age_days(self):  # Creates a method of calculating age in days
        return f"{self.name} is {self.age * 365} days old."


# These are two different Dof objects
dog1 = Dog("Spot", 7, "black", "savage")
dog2 = Dog("Jazz", 5, "white", "playful")
dog3 = Dog("Boss", 9, "ginger", "biting")

# Calling for the print_details method for each dog object
print(Dog.print_details(dog1))
print(Dog.print_details(dog2))
print(Dog.print_details(dog3))
print(Dog.age_days(dog1))
print(Dog.age_days(dog2))
print(Dog.age_days(dog3))

