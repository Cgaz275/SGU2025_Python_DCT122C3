# student_manager.py
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_all(self):
        for s in self.students:
            s.display_info()

    def delete_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                return True
        return False

    def update_student(self, student_id, name=None, gender=None, age=None, birthplace=None, major=None):
        for s in self.students:
            if s.student_id == student_id:
                if name: s._name = name
                if gender: s._gender = gender
                if age: s._age = age
                if birthplace: s._birthplace = birthplace
                if major: s.major = major
                return True
        return False

    def search_by_name(self, keyword):
        result = [s for s in self.students if keyword.lower() in s.get_name().lower()]
        return result

    def count_gender(self):
        male = sum(1 for s in self.students if s.get_gender().lower() == 'nam')
        female = sum(1 for s in self.students if s.get_gender().lower() == 'nữ')
        return male, female

    def average_age(self):
        if not self.students:
            return 0
        return sum(s.get_age() for s in self.students) / len(self.students)

    def birthplaces(self):
        places = {}
        for s in self.students:
            place = s.get_birthplace()
            places[place] = places.get(place, 0) + 1
        return places
