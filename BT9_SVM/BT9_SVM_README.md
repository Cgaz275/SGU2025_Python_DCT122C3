## 1. SVM là gì? 

**Support Vector Machine** là một thuật toán học máy có giám sát dùng để **phân loại** (và hồi quy).

Ý tưởng cốt lõi:
> **Tìm đường biên (hyperplane) sao cho khoảng cách từ đường biên đó tới các điểm gần nhất của 2 lớp là lớn nhất có thể.**

- Khoảng cách này gọi là **Margin** → SVM luôn muốn **margin rộng nhất** → mô hình bền vững, ít bị nhiễu.
- Các điểm nằm sát mép margin → gọi là **Support Vectors** 
- Khi dữ liệu không phân tách được bằng đường thẳng → dùng **Kernel Trick** để “nhấc” dữ liệu lên không gian cao chiều → vẫn tìm được hyperplane.

### Công thức chính 

1. **Hard-margin SVM** 
   Tối ưu:  
   $$
   \max_{\mathbf{w},b} \ \frac{2}{\|\mathbf{w}\|} \quad \text{với} \quad y_i(\mathbf{w}^T\mathbf{x}_i + b) \geq 1 \ \forall i
   $$

2. **Soft-margin SVM** 
   $$
   \min_{\mathbf{w},b,\xi} \ \frac{1}{2}\|\mathbf{w}\|^2 + C \sum \xi_i
   $$
   - Tham số `C`: càng lớn → càng phạt nặng các điểm vi phạm margin (giống như độ “nghiêm khắc”).

3. **Kernel Trick**  
   Thay vì tính trực tiếp trong không gian cao chiều, ta dùng hàm kernel:  
   $$
   K(\mathbf{x}_i, \mathbf{x}_j) = \phi(\mathbf{x}_i)^T \phi(\mathbf{x}_j)
   $$
   Phổ biến nhất:
   - `linear` → \( K = \mathbf{x}_i^T \mathbf{x}_j \)
   - `rbf` (Gaussian) → \( K = \exp(-\gamma \|\mathbf{x}_i - \mathbf{x}_j\|^2) \)

## 2. Các thuật ngữ quan trọng

| Thuật ngữ             | Giải thích đơn giản                                    |
|-----------------------|--------------------------------------------------------|
| Hyperplane            | Đường phân cách (đường thẳng 2D, mặt phẳng 3D…)        |
| Margin                | Khoảng cách từ hyperplane tới điểm gần nhất           |
| Support Vectors       | Các điểm nằm sát margin → quyết định mô hình           |
| Hard Margin           | Không cho phép điểm nào nằm trong margin               |
| Soft Margin           | Cho phép một ít điểm sai (điều chỉnh bằng tham số C)   |
| Kernel Trick          | “Nhấc” dữ liệu lên không gian cao hơn mà không cần tính trực tiếp |

## 3. Thư viện & hàm đã dùng trong code

| Thư viện       | Mục đích                            | Hàm quan trọng sử dụng                          |
|----------------|-------------------------------------|-------------------------------------------------|
| `numpy`        | Tính toán mảng                      | `np.array`, `np.linspace`, `np.meshgrid`        |
| `matplotlib.pyplot` | Vẽ đồ thị                      | `plt.scatter`, `plt.plot`, `plt.contourf`       |
| `sklearn.svm`  | Mô hình SVM                         | `SVC(kernel=..., C=..., gamma=...)`             |
| `sklearn.datasets` | Tạo dữ liệu mẫu                 | `make_circles`                                  |

### Các tham số thường chỉnh trong `SVC()`
- `kernel`: `'linear'`, `'rbf'`, `'poly'`, ...
- `C`: độ “nghiêm khắc” (C lớn → ít lỗi hơn, dễ overfit)
- `gamma`: chỉ dùng với kernel RBF → ảnh hưởng độ cong của biên (gamma lớn → biên “lắt léo” hơn)

