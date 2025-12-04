# 1. Yêu cầu bài tập

Sử dụng OOP viết chương trình quản lý sinh viên đơn giản ( thể hiện đầy đủ đóng gói, kế thừa, đa hình, trừu tượng), tính tổng sinh viên nam,nữ, độ tuổi, nơi sinh

## 2. Giới thiệu

Đây là chương trình quản lý sinh viên viết bằng Python, áp dụng đầy đủ bốn tính chất OOP:

- Đóng gói (Encapsulation)
- Kế thừa (Inheritance)
- Đa hình (Polymorphism)
- Trừu tượng (Abstraction)

Chương trình hỗ trợ:

- Thêm sinh viên
- Xóa sinh viên
- Sửa thông tin
- Tìm kiếm theo tên
- Hiển thị danh sách
- Thống kê
- Lưu và tải dữ liệu từ JSON


## 3. Cấu trúc thư mục
<pre>

BT2_PythonOOP/
│
├── person.py
├── student.py
├── student_manager.py
├── data_manager.py
├── main.py
└── studentdata.json

</pre>

## 4. Bảng giải thích các file trong project

| File | Vai trò | Nội dung chính | Liên quan đến OOP |
|---|---|---|---|
| **person.py** | Định nghĩa lớp trừu tượng Person | Chứa các thuộc tính chung (tên, giới tính, tuổi, nơi sinh) và phương thức trừu tượng `display_info()` | **Trừu tượng**, **Đóng gói** |
| **student.py** | Định nghĩa lớp Student | Kế thừa Person, thêm các thuộc tính student_id và major, override `display_info()` | **Kế thừa**, **Đa hình** |
| **student_manager.py** | Bộ quản lý sinh viên | Chứa các chức năng thêm, xóa, sửa, tìm kiếm, thống kê danh sách sinh viên | Áp dụng OOP để thao tác trên đối tượng Student |
| **data_manager.py** | Quản lý dữ liệu JSON | Lưu danh sách sinh viên vào file và đọc dữ liệu từ file JSON | Hỗ trợ lưu trữ, không trực tiếp là OOP |
| **main.py** | Chương trình chính | Chứa menu tương tác, xử lý nhập liệu, gọi StudentManager và DataManager | Điều phối toàn bộ hệ thống OOP |
| **studentdata.json** | File dữ liệu | Lưu danh sách sinh viên dưới dạng JSON | Không phải OOP, chỉ là nơi lưu trữ |
## 5. Các tính chất OOP được áp dụng như thế nào?

#### 5.1. Đóng gói (Encapsulation)
Các thuộc tính của lớp `Person` được khai báo ở dạng protected (`_name`, `_gender`, `_age`, `_birthplace`) và được truy cập thông qua các phương thức getter.  
Điều này giúp ẩn dữ liệu và kiểm soát cách truy cập.

Ví dụ:
```python
self._name = name

def get_name(self):
    return self._name
```
#### 5.2. Kế thừa (Inheritance)
Lớp Student kế thừa từ lớp `Person`, giúp tái sử dụng mã nguồn và mở rộng thêm thuộc tính mới như `student_id`, `major`.

```python
class Student(Person):
    def __init__(self, name, gender, age, birthplace, student_id, major):
        super().__init__(name, gender, age, birthplace)
        self.student_id = student_id
        self.major = major

```

#### 5.3. Đa hình (Polymorphism)

```python
def display_info(self):
    print(f"Name: {self._name}")
    print(f"Gender: {self._gender}")
    print(f"Age: {self._age}")
    print(f"Birthplace: {self._birthplace}")
    print(f"Student ID: {self.student_id}")
    print(f"Major: {self.major}")

```

#### 5.4. Trừu tượng (Abstraction)


```python
from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def display_info(self):
        pass

```
