# data_manager.py
import json

class DataManager:

    @staticmethod
    def save_to_json(filename, students):
        data = []
        for s in students:
            data.append({
                "name": s.get_name(),
                "gender": s.get_gender(),
                "age": s.get_age(),
                "birthplace": s.get_birthplace(),
                "student_id": s.student_id,
                "major": s.major
            })

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def load_from_json(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
