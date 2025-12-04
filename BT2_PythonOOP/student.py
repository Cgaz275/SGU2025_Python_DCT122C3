# student.py
from person import Person

class Student(Person):
    def __init__(self, name, gender, age, birthplace, student_id, major):
        super().__init__(name, gender, age, birthplace)
        self.student_id = student_id
        self.major = major

    # Đa hình: override phương thức trừu tượng
    def display_info(self):
        print(f"--- Student Info ---")
        print(f"Name: {self._name}")
        print(f"Gender: {self._gender}")
        print(f"Age: {self._age}")
        print(f"Birthplace: {self._birthplace}")
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        print("---------------------\n")
