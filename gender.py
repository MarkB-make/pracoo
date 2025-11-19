ALL_COURSES = [
    "Data Science",
    "Software Engineering",
    "DevOPS",
    "Cyber Security",
    "AI Engineering",
    "High School Bootcamp",
    "Product Design",
    "Data Analytics",
    "Data Analytics for HR Professionals",
]


class Student:
    student_count = 0
    all_students = []

    def __init__(self, first_name, last_name, age, gender, student_id, course, instructor):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student_id = student_id
        self.course = course
        self.instructor = instructor

        Student.student_count += 1
        Student.all_students.append(self)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value.strip():
            raise ValueError("First name cannot be empty.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value.strip():
            raise ValueError("Last name cannot be empty.")
        self._last_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value not in ["Male", "Female"]:
            raise ValueError("Gender must be 'Male' or 'Female'.")
        self._gender = value

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course):
        if course not in ALL_COURSES:
            raise ValueError(f"'{course}' is NOT a valid course.")
        self._course = course

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@student.moringaschool.com"

    @classmethod
    def total_students(cls):
        return f"The total number of students is: {cls.student_count}"

    @classmethod
    def student_list(cls):
        return [f"{student.first_name} {student.last_name}" for student in cls.all_students]

    @classmethod
    def student_list_2(cls):
        return [student.fullname for student in cls.all_students]

    @staticmethod
    def reverse_name(first_name, last_name):
        return f"{last_name} {first_name}"


student1 = Student("Bradley", "Murimi", 40, "Male", "MSS-1234", "Software Engineering", "Fainus Mudahe")
student2 = Student("Mariam", "Rashid", 20, "Female", "MSS-1428", "Software Engineering", "Julius Mutindwa")
student3 = Student("Fredrick", "Rangara", 50, "Male", "MSS-1480", "Software Engineering", "Julius Mutindwa")
student4 = Student("Adonis", "Pierre", 30, "Male", "MSS-3445", "Data Analytics", "Julius Mutindwa")

print(student4.gender)