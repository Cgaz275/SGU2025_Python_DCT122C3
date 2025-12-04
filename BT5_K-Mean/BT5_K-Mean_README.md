# Phân cụm khách hàng trung tâm thương mại bằng thuật toán K-Means  
**Bài tập thực hành Machine Learning – K-Means Clustering**  
Dữ liệu: `Mall_Customers.csv` (200 khách hàng)

---

### 1. Tổng quan về thuật toán K-Means

**K-Means** là một trong những thuật toán phân cụm (clustering) không giám sát phổ biến nhất.  
Mục tiêu: Chia dữ liệu thành **K cụm** sao cho các điểm trong cùng một cụm gần nhau nhất có thể và các cụm cách xa nhau nhất có thể.

#### Các bước hoạt động của K-Means
1. Chọn ngẫu nhiên K điểm làm **tâm cụm (centroids)** ban đầu  
2. Gán mỗi điểm dữ liệu vào cụm có tâm gần nhất (khoảng cách Euclidean)  
3. Cập nhật lại tâm cụm = trung bình cộng của tất cả các điểm thuộc cụm đó  
4. Lặp lại bước 2–3 cho đến khi tâm cụm không thay đổi (hoặc thay đổi rất ít)

#### Công thức chính
- **Khoảng cách Euclidean**:  
  \( d(x, \mu) = \sqrt{\sum_{j=1}^{d} (x_j - \mu_j)^2} \)
- **Tâm cụm mới**:  
  \( \mu_i = \frac{1}{|C_i|} \sum_{x \in C_i} x \)
- **Hàm mục tiêu (Inertia / WSS – Within-cluster Sum of Squares)**:  
  \( J = \sum_{i=1}^{K} \sum_{x \in C_i} \| x - \mu_i \|^2 \)  
  → K-Means cố gắng **tối thiểu hóa J**

#### Inertia là gì?
- Là tổng bình phương khoảng cách từ các điểm đến tâm cụm gần nhất  
- Giá trị càng nhỏ → phân cụm càng tốt  
- Dùng để vẽ **Elbow Method** chọn K tối ưu

#### Elbow Method
- Chạy K-Means với K từ 1 đến n (thường 10)  
- Vẽ đồ thị Inertia theo K  
- Chọn K tại điểm **"khuỷu tay"** – nơi đường cong giảm mạnh rồi chậm dần

---

### 2. Các thư viện & hàm đã sử dụng

| Thư viện           | Mục đích chính                                 | Các hàm quan trọng đã dùng                              | Ý nghĩa |
|-------------------|--------------------------------------------------|---------------------------------------------------------|--------|
| `pandas`          | Đọc, xử lý dữ liệu bảng                          | `pd.read_csv()`, `.rename()`, `.head()`, `.groupby().agg()` | Xử lý file CSV, đổi tên cột, tính thống kê |
| `numpy`           | Tính toán mảng số học                            | (hỗ trợ backend)                                        | Hỗ trợ tính toán nhanh |
| `matplotlib.pyplot` | Vẽ biểu đồ cơ bản                              | `plt.figure()`, `plt.scatter()`, `plt.plot()`, `plt.show()` | Vẽ scatter plot, Elbow curve |
| `seaborn`         | Vẽ biểu đồ đẹp hơn matplotlib                   | `sns.scatterplot()`                                     | Tạo biểu đồ phân cụm màu sắc đẹp |
| `sklearn.preprocessing` | Chuẩn hóa dữ liệu                          | `StandardScaler().fit_transform()`                      | Đưa các đặc trưng về cùng thang đo (rất quan trọng khi Age và Income khác nhau lớn) |
| `sklearn.cluster` | Thực thi thuật toán K-Means                      | `KMeans(n_clusters=k, random_state=42, n_init=10)`<br>`.fit_predict()`<br>`.cluster_centers_`<br>`.inertia_` | Tạo mô hình, phân cụm, lấy tâm cụm, lấy giá trị Inertia |

> Lưu ý: `n_init=10` → chạy thuật toán 10 lần với các khởi tạo khác nhau → chọn kết quả tốt nhất (giảm rủi ro rơi vào local minima)

---

### 3. Hai ví dụ thực hiện trong notebook

| Ví dụ | Đặc trưng sử dụng         | K tối ưu (qua Elbow) | Số cụm đã chọn | Nhận xét nổi bật |
|------|----------------------------|----------------------|----------------|------------------|
| 1    | `Income` + `Spending Score`| K=5                  | 5              | Kết quả kinh điển, 5 nhóm rất rõ ràng (VIP, Tiết kiệm, Cẩn thận…) |
| 2    | `Age` + `Spending Score`   | K=4                  | 4              | Nhóm trẻ chi tiêu cao, nhóm lớn tuổi chi tiêu thấp… |

**Kết luận quan trọng cho bài tập**:  
→ **Mỗi khi thay đổi tập hợp đặc trưng → phải vẽ lại Elbow → K tối ưu thay đổi!**

---

### 4. Cấu trúc file

```
├── Mall_Customers.csv          → Dữ liệu gốc (200 khách hàng)
├── kmean.ipynb                 → Notebook chính (có 2 ví dụ + Elbow)
├── README.md                   → File bạn đang đọc
└── (các hình ảnh scatter plot và Elbow sẽ tự động hiện trong notebook)
```

### 5. Thông tin Dataset: Mall Customer Segmentation Data

**Nguồn**: [Kaggle - Customer Segmentation Tutorial in Python](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)  
**Tác giả**: VJ Choudhary (đăng tải năm 2017, cập nhật gần nhất 2023)  
**Mô tả tổng quan**:  
Bộ dữ liệu chứa thông tin về hành vi mua sắm của 200 khách hàng tại một trung tâm thương mại (mall). Dữ liệu được sử dụng phổ biến để minh họa phân khúc khách hàng (customer segmentation) bằng các thuật toán clustering như K-Means. Nó giúp phân tích các nhóm khách hàng dựa trên thu nhập, chi tiêu và độ tuổi, hỗ trợ chiến lược marketing (ví dụ: ưu đãi cho nhóm "VIP" chi tiêu cao).

#### Đặc điểm chính của Dataset
| Thuộc tính          | Giá trị                  | Ý nghĩa |
|---------------------|--------------------------|---------|
| **Kích thước file** | ~3 KB (CSV)              | Nhỏ gọn, dễ tải và xử lý |
| **Số lượng mẫu**    | 200 hàng (khách hàng)    | Đủ lớn để demo, không quá phức tạp |
| **Số cột**          | 5 cột                    | Tập trung vào các đặc trưng chính |
| **Loại dữ liệu**    | Hỗn hợp: Categorical (Gender), Numerical (Age, Income, Spending) | Cần xử lý encoding nếu dùng ML nâng cao |

#### Cấu trúc các cột dữ liệu
| Tên cột gốc                  | Tên cột sau rename (trong code) | Ý nghĩa | Phạm vi/Giá trị mẫu |
|------------------------------|---------------------------------|---------|---------------------|
| `CustomerID`                 | `CustomerID`                    | ID duy nhất của khách hàng | 1 → 200 (integer) |
| `Gender`                     | `Gender`                        | Giới tính | 'Male', 'Female' (categorical) |
| `Age`                        | `Age`                           | Độ tuổi | 18 → 70 (integer) |
| `Annual Income (k$)`         | `Income`                        | Thu nhập hàng năm (nghìn USD) | 15 → 137 (integer) |
| `Spending Score (1-100)`     | `Spending`                      | Điểm chi tiêu (dựa trên hành vi mua sắm) | 1 → 99 (integer) |

#### Thống kê cơ bản (từ dữ liệu gốc)
- **Phân bố Gender**: ~55% Female, ~45% Male  
- **Tuổi trung bình**: ~38-40 tuổi (phù hợp với khách hàng trung tâm thương mại)  
- **Thu nhập trung bình**: ~60-70 k$/năm  
- **Điểm chi tiêu trung bình**: ~50/100 (phân bố đều, dễ phân cụm)  
- **Không có giá trị thiếu**: Dataset sạch, sẵn sàng sử dụng  
