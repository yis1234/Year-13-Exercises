class Student:
    def __init__(self, name, age, phone_number, form_class, subjects, is_male, enrolled):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.form_class = form_class
        self.subjects = subjects
        self.is_male = is_male == "male"
        self.enrolled = True
        student_list.append(self)
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Form Class: {self.form_class}")
        print(f"Subjects: {self.subjects}")
        print(f"Is Male: {self.is_male}")
        print(f"Enrolled: {self.enrolled}")
    
    def change_info(self):
        self.name = input("Enter the new name: ").title()
        self.age = input("Enter the new age: ")
        self.phone_number = input("Enter the new phone number: ")
        self.form_class = input("Enter the new form class: ")


def generate_students():
    import csv
    with open('random_students.csv', newline= '') as csvfile:
        filereader = csv.reader(csvfile, delimiter='|')
        for line in filereader:
            if line[5] == "True":
                is_male = "male"
            else:
                is_male = "female"
            Student(line[0], line[1], line[2], line[3], line[4], is_male, True)
            student_list.append(Student(line[0], line[1], line[2], line[3], line[4], is_male, True))


def print_student_details():
    for student in student_list:
        student.display_info()


def select_student_age():
    age = input("Enter the age of students you want to know: ")
    for student in student_list:
        if student.age >= age:
            student.display_info()
        else:
            print(f"{student.name} is {age} or older")


def count_students():
    subject = input("What class are you looking for: ")
    # count how many students there are in a subject
    count = 0
    for student in student_list:
        if student.subjects == subject:
            count += 1
    print(count)



student_list = []
generate_students()

print(student_list)
# print_student_details()
# select_student_age()
count_students()