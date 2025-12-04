# main.py
from student import Student
from student_manager import StudentManager
from data_manager import DataManager

FILENAME = "BT2_PythonOOP/studentdata.json"

manager = StudentManager()

# Load dữ liệu từ JSON
loaded = DataManager.load_from_json(FILENAME)
for item in loaded:
    sv = Student(
        item["name"],
        item["gender"],
        item["age"],
        item["birthplace"],
        item["student_id"],
        item["major"]
    )
    manager.add_student(sv)


def save_now():
    DataManager.save_to_json(FILENAME, manager.students)


def input_student():
    name = input("Tên: ")
    gender = input("Giới tính (Nam/Nữ): ")
    age = int(input("Tuổi: "))
    birthplace = input("Nơi sinh: ")
    student_id = input("Mã sinh viên: ")
    major = input("Chuyên ngành: ")
    return Student(name, gender, age, birthplace, student_id, major)


while True:
    print("\n===== MENU QUẢN LÝ SINH VIÊN =====")
    print("1. Thêm sinh viên")
    print("2. Xóa sinh viên")
    print("3. Sửa thông tin sinh viên")
    print("4. Tìm kiếm theo tên")
    print("5. Xem danh sách sinh viên")
    print("6. Thống kê")
    print("0. Thoát")
    print("\n=====================")
    choice = input("Chọn: ")
    

    if choice == "1":
        sv = input_student()
        manager.add_student(sv)
        save_now()
        print("Đã thêm và lưu dữ liệu.")

    elif choice == "2":
        sid = input("Nhập mã sinh viên cần xóa: ")
        if manager.delete_student(sid):
            save_now()
            print("Đã xóa và lưu dữ liệu.")
        else:
            print("Không tìm thấy sinh viên.")

    elif choice == "3":
        sid = input("Mã sinh viên cần sửa: ")
        print("Nhập thông tin mới (bỏ trống để giữ nguyên):")
        name = input("Tên: ")
        gender = input("Giới tính: ")
        age = input("Tuổi: ")
        birthplace = input("Nơi sinh: ")
        major = input("Chuyên ngành: ")

        updated = manager.update_student(
            sid,
            name=name if name else None,
            gender=gender if gender else None,
            age=int(age) if age else None,
            birthplace=birthplace if birthplace else None,
            major=major if major else None,
        )

        if updated:
            save_now()
            print("Đã sửa và lưu dữ liệu.")
        else:
            print("Không tìm thấy sinh viên.")

    elif choice == "4":
        keyword = input("Nhập tên cần tìm: ")
        result = manager.search_by_name(keyword)
        if result:
            for s in result:
                s.display_info()
        else:
            print("Không tìm thấy sinh viên.")

    elif choice == "5":
        manager.show_all()

    elif choice == "6":
        male, female = manager.count_gender()
        print(f"Số sinh viên nam: {male}")
        print(f"Số sinh viên nữ: {female}")
        print(f"Độ tuổi trung bình: {manager.average_age():.2f}")
        print("Thống kê nơi sinh:")
        for p, c in manager.birthplaces().items():
            print(f"- {p}: {c}")

    elif choice == "0":
        print("Chương trình kết thúc.")
        break

    else:
        print("Lựa chọn không hợp lệ.")
