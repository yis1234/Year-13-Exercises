class AllStaff():
    def __init__(self, name, age, id, birthdate, job):
        self.name = name
        self.age = age
        self.id = id
        self.birthdate = birthdate
        self.job = job
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.id}")
        print(f"Birthdate: {self.birthdate}")
        print(f"Job: {self.job}")


class Management(AllStaff):
    def __init__(self, name, age, id, birthdate, job, car):
        super().__init__(name, age, id, birthdate, job)
        self.car = car

    def display_info(self):
        super().display_info()
        print(f"Car: {self.car}")


class Clerical(AllStaff):
    def __init__(self, name, age, id, birthdate, job, typing_speed):
        super().__init__(name, age, id, birthdate, job)
        self.typing_speed = typing_speed

    def display_info(self):
        super().display_info()
        print(f"Clinic: {self.typing_speed}")


class Factory(AllStaff):
    pass


# Main Routine
