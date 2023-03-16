class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # integer between 1-100


    def get_grade(self):
        return self.grade

        
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  # blank list to hold enrolled students
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
        return total / len(self.students)

# Instantiate 3 student objects
s1 = Student("Tim", 19, 95)
s2 = Student("Joy", 19, 75)
s3 = Student("Jill", 19, 65)


# Instantiate course object
course1 = Course("Computer Science", 3)

# Add students to course
course1.add_student(s1)
course1.add_student(s2)
course1.add_student(s3)

# Get average grade
print(f"The average grade for {course1.name} is {course1.get_average_grade()}")

# Confirm entry of students
for student in course1.students:
    print(student.name)