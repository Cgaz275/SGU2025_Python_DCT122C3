# Minh họa Thuật toán K-Nearest Neighbors (KNN)  
## Hai ví dụ thực tế gắn với đời sống Việt Nam

### 1. Giới thiệu chung
Dự án này minh họa thuật toán **K-Nearest Neighbors (KNN)** – một thuật toán học máy có giám sát đơn giản và hiệu quả – thông qua hai bài toán phân loại nhị phân gần gũi:

1. **Dự đoán sở thích món ăn**: Phở hay Bún bò Huế  
   → Đặc trưng: mức độ thích mặn và mức độ thích cay (thang 1–10).

2. **Dự đoán phương tiện di chuyển**: GrabBike hay GrabCar  
   → Đặc trưng: khoảng cách di chuyển (km) và ngân sách sẵn chi (nghìn đồng).

Mục tiêu: giúp người học nắm rõ bản chất, cơ chế hoạt động và cách trực quan hóa kết quả của KNN.

### 2. Khái niệm K-Nearest Neighbors (KNN)

KNN là thuật toán phân loại (hoặc hồi quy) dựa trên nguyên tắc **đa số quyết định** từ **k** điểm dữ liệu gần nhất trong không gian đặc trưng.

- **Phân loại**: Nhãn của điểm mới = nhãn xuất hiện nhiều nhất trong k láng giềng (majority voting).  
- **Hồi quy**: Giá trị dự đoán = trung bình (hoặc trung vị) của k láng giềng.

#### Công thức khoảng cách Euclidean (sử dụng trong ví dụ này):
$$
d(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}
$$
Trong đó:  
- \(x, y\): hai vectơ đặc trưng  
- \(n\): số chiều (số đặc trưng)

### 3. Dữ liệu sử dụng

| Ví dụ                  | Số mẫu huấn luyện | Số đặc trưng | Nhãn lớp               |
|------------------------|-------------------|--------------|------------------------|
| Phở vs Bún bò Huế      | 8                 | 2            | Phở / Bún bò           |
| GrabBike vs GrabCar    | 10                | 2            | GrabBike / GrabCar     |

Điểm cần dự đoán được đánh dấu `?` trong cột nhãn.

### 4. Các thư viện sử dụng

| Thư viện                  | Chức năng chính trong dự án                                |
|---------------------------|------------------------------------------------------------|
| `pandas`                  | Xử lý và lưu trữ dữ liệu dạng bảng                         |
| `numpy`                   | Tính toán số học và mảng đa chiều                          |
| `matplotlib`              | Vẽ biểu đồ scatter và đường nối láng giềng                 |
| `seaborn`                 | Cải thiện thẩm mỹ đồ họa                                   |
| `scikit-learn` (`KNeighborsClassifier`) | Triển khai thuật toán KNN                  |

#### Các hàm/lớp chính được sử dụng

| Hàm / Lớp                                           | Ý nghĩa                                                      |
|-----------------------------------------------------|--------------------------------------------------------------|
| `KNeighborsClassifier(n_neighbors=k)`               | Khởi tạo mô hình KNN với k láng giềng                        |
| `.fit(X_train, y_train)`                            | Huấn luyện (KNN là lazy learner – chỉ lưu dữ liệu)           |
| `.predict(X_new)`                                   | Dự đoán nhãn cho điểm mới                                    |
| `.kneighbors(X_new, n_neighbors=k, return_distance=False)` | Trả về chỉ số của k láng giềng gần nhất (dùng để vẽ đồ thị) |

### 5. Cấu trúc dự án
```
├── KNN.ipynb    ← Notebook chính (đã nhúng dữ liệu, chạy ngay)
├── README.md                     
```

