# person.py
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, gender, age, birthplace):
        self._name = name            # đóng gói (private/protected)
        self._gender = gender
        self._age = age
        self._birthplace = birthplace

    # Getter & Setter (Đóng gói)
    def get_name(self):
        return self._name

    def get_gender(self):
        return self._gender

    def get_age(self):
        return self._age

    def get_birthplace(self):
        return self._birthplace

    @abstractmethod
    def display_info(self):
        """Phương thức trừu tượng — buộc lớp con override"""
        pass
