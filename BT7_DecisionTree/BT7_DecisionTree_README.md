## 1. Mục tiêu bài tập
- Hiểu cách hoạt động của thuật toán Cây quyết định (Decision Tree)
- Thực hành xây dựng, trực quan hóa và dự đoán bằng DecisionTreeClassifier của scikit-learn
- Trình bày 2 ví dụ thực tế đơn giản, trực quan, dễ hiểu

## 2. Nội dung thư mục

```
├── tennis.csv              ← Dữ liệu ví dụ 1: Có nên chơi tennis không?
├── fruit.csv               ← Dữ liệu ví dụ 2: Phân loại trái cây
├── BT7_DecisionTree.py     ← Code Python hoàn chỉnh (chạy được ngay)
├── README.md               
```


## 3. Hai ví dụ được thực hiện
```
### Ví dụ 1 – Chơi tennis (Play Tennis)
- Dữ liệu kinh điển 14 ngày với 4 thuộc tính: Thời tiết, Nhiệt độ, Độ ẩm, Gió
- Mục tiêu: Dự đoán có chơi tennis hay không
- Sử dụng tiêu chí Entropy (Information Gain)

### Ví dụ 2 – Phân loại trái cây
- 10 mẫu trái cây với 4 thuộc tính: Màu sắc, Kích thước, Hình dạng, Trọng lượng
- Mục tiêu: Phân loại thành Cherry, Táo, Dưa hấu, Chuối, Dưa leo
- Sử dụng tiêu chí Gini
```

### 4. Định nghĩa Cây Quyết Định (Decision Tree)


**Định nghĩa & nguyên lý hoạt động của Cây quyết định**

Cây quyết định (Decision Tree) là một mô hình học máy có giám sát được sử dụng cho cả bài toán phân loại (classification) và hồi quy (regression).  
Trong bài tập này chúng ta chỉ xét Decision Tree Classification.

Cấu trúc:
- Nút gốc (Root Node): đại diện toàn bộ tập dữ liệu
- Nút nội bộ (Internal Node): kiểm tra một thuộc tính
- Nhánh (Branch): kết quả của phép kiểm tra
- Nút lá (Leaf Node): chứa nhãn lớp cuối cùng (quyết định)

Nguyên lý:
Thuật toán sẽ chọn liên tục thuộc tính “tốt nhất” để chia dữ liệu thành các tập con thuần khiết hơn (các mẫu cùng lớp càng nhiều càng tốt).  

### 5. Giới thiệu 2 bộ dữ liệu thực hành

**Tập dữ liệu 1 - `tennis.csv`**
- Nguồn: Quinlan, J. R. (1986) – bài báo khởi nguồn của C4.5
- Số mẫu: 14 ngày
- Thuộc tính (4):
  - Thời tiết (Nắng / Mây / Mưa)
  - Nhiệt độ (Nóng / Nhẹ / Mát)
  - Độ ẩm (Cao / Bình thường)
  - Gió (Có / Không)
- Nhãn: Chơi tennis? (Có / Không)
- Mục đích: Minh họa cách cây quyết định tự động học các quy tắc như “Nếu trời Nắng và Độ ẩm Cao thì Không chơi”.

**Tập dữ liệu 2 - `fruit.csv`**
- Nguồn: tự xây dựng
- Số mẫu: 10 trái cây
- Thuộc tính (4):
  - Màu sắc (Đỏ / Xanh / Vàng)
  - Kích thước (Nhỏ / Trung bình / Lớn)
  - Hình dạng (Tròn / Dài)
  - Trọng lượng (Nhẹ / Nặng)
- Nhãn: Cherry – Táo – Dưa hấu – Chuối – Dưa leo
- Mục đích: Rất dễ hình dung, cây chỉ sâu 2–3 tầng đã đạt độ chính xác 100%.