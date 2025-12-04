# Yêu cầu bài tập 

10 ví dụ về Pandas, đọc ghi file csv,text,json, xlsx, xử lý dataframe 10 chủ đề nhỏ với 2 ví dụ của mỗi chủ đề với numpy

### 1. Các chủ đề được trình bày

| Nhóm Chức Năng | Ví dụ | Cú pháp NumPy | Kết quả/Mô tả |
| :--- | :--- | :--- | :--- |
| **Thống Kê Cơ Bản** | Trung bình số lượng | `np.mean(sl)` | 92.5 cái |
| | Độ lệch chuẩn đơn giá | `np.std(dg)` | 6,715,836 đ |
| --- | --- | --- | --- |
| **Tính Toán Mảng** | **Tổng giá trị tồn kho** | `np.sum(sl * dg)` | 1,981,550,000 đ |
| | Trung vị (Median) số lượng | `np.median(sl)` | 35.0 cái |
| --- | --- | --- | --- |
| **Giá Trị Cực Đại/Tiểu** | Đơn giá cao nhất | `np.max(dg)` | 28,900,000 đ (iPhone 15 Pro) |
| | Phạm vi (Range) số lượng | `np.max(sl) - np.min(sl)` | 395 cái |
| --- | --- | --- | --- |
| **Tương Quan** | Hệ số Pearson | `np.corrcoef(sl, dg)[0,1]` | -0.3 (xu hướng âm) |
| | Hiệp phương sai (Covariance) | `np.cov(sl, dg)[0,1]` | Tính độ biến thiên chung |
| --- | --- | --- | --- |
| **Lọc Mảng (Indexing)** | Sản phẩm giá > 5 triệu | `dg[dg > 5000000]` | Trả về mảng giá cao |
| | Số lượng > 100 | `sl[sl > 100]` | Trả về mảng số lượng lớn |
| --- | --- | --- | --- |
| **Sắp Xếp & Vị Trí** | Sắp xếp đơn giá tăng dần | `np.sort(dg)` | Sắp xếp mảng |
| | **Index** sản phẩm đắt nhất | `np.argmax(dg)` | Trả về vị trí (index) |
| --- | --- | --- | --- |
| **Tính Toán Toàn Cầu**| **Trung bình có trọng số** | `np.average(dg, weights=sl)` | Đơn giá trung bình có trọng số tồn |
| | Tổng số lượng | `np.sum(sl)` | Tổng số lượng của tất cả mặt hàng |
| --- | --- | --- | --- |
| **Phân Phối** | **Percentile 75%** | `np.percentile(sl, 75)` | 135 cái |
| | Biểu đồ tần suất (Histogram) | `np.histogram(sl, bins=5)` | Phân bố tần suất |
| --- | --- | --- | --- |
| **Ma Trận** | Tạo ma trận từ 2 mảng | `np.array([sl, dg])` | Tạo ma trận |
| | Nhân ma trận (tổng giá trị) | `np.dot(sl, dg)` | Kết quả tương đương `np.sum(sl * dg)` |
| --- | --- | --- | --- |
| **Tìm Kiếm Nhanh** | Index sản phẩm Logitech | `np.where(df['TenSP'].str.contains('Logitech'))` | Trả về index thỏa mãn điều kiện |
| | Mask lọc kết hợp | `mask = np.logical_and(sl > 100, dg < 2000000)` | Trả về **Boolean mask** (sản phẩm tồn nhiều giá rẻ) |

### 2. Bảng tổng hợp các hàm đã dùng và công thức (nếu có)

| STT | Thư viện | Hàm / Phương thức | Mô tả / Công dụng thực tế | Công thức toán | Ví dụ thực tế trong dữ liệu kho hàng |
| :---: | :---: | :--- | :--- | :--- | :--- |
| 1 | `pandas` | `pd.read_excel()` | Đọc file Excel (`tong_hop.xlsx`) | - | `df = pd.read_excel('tong_hop.xlsx', sheet_name='DuLieuGoc')` |
| 2 | `pandas` | `pd.read_csv()` | Đọc file CSV (có thể có dấu phẩy hoặc chấm phẩy) | - | `pd.read_csv('xuat_kho_chon_loc.csv')` |
| 3 | `pandas` | `pd.read_json()` | Đọc file JSON (`don_hang.json`) | - | `pd.read_json('don_hang.json')` |
| 4 | `pandas` | `df.to_excel()`, `df.to_csv()`, `df.to_json()` | Ghi DataFrame ra file | - | `df.to_excel('ketqua.xlsx', index=False)` |
| 5 | `pandas` | `df.head(n)` | Xem **n dòng đầu** | - | `df.head(3)` |
| 6 | `pandas` | `df['col'].values` | Chuyển cột thành mảng **NumPy** | - | `sl = df['SoLuong'].values` |
| 7 | `pandas` | `df.loc[idx]` | Lấy dòng theo index (dùng để lấy tên sản phẩm đắt nhất) | - | `df.loc[np.argmax(dg), 'TenSP']` |
| 8 | `pandas` | `df.query("điều_kiện")` | Truy vấn siêu nhanh (cú pháp giống SQL) | - | `df.query("SoLuong > 100 and DonGia < 2000000")` |
| 9 | `pandas` | `df['col'].str.contains()` | Tìm chuỗi trong cột văn bản | - | `df['TenSP'].str.contains('Logitech')` |
| 10 | `pandas` | `df.groupby().agg()` | Nhóm và tính tổng/trung bình… | - | `df.groupby('NhomHang')['SoLuong'].sum()` |
| 11 | `NumPy` | `np.mean(arr)` | **Trung bình cộng** | $\bar{x} = \frac{\sum x_i}{n}$ | `np.mean(sl)` → 92.5 cái |
| 12 | `NumPy` | `np.median(arr)` | **Trung vị** | - | `np.median(sl)` → 35.0 |
| 13 | `NumPy` | `np.std(arr)` | **Độ lệch chuẩn** | $\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n}}$ | `np.std(sl)` → ~107.1 |
| 14 | `NumPy` | `np.var(arr)` | **Phương sai** | $\sigma^2 = \frac{\sum (x_i - \bar{x})^2}{n}$ | - |
| 15 | `NumPy` | `np.min(arr)`, `np.max(arr)` | Giá trị nhỏ nhất/lớn nhất | - | `np.max(dg)` → 28,900,000 (iPhone 15 Pro) |
| 16 | `NumPy` | `np.argmax(arr)`, `np.argmin(arr)` | **Vị trí (index)** của giá trị lớn nhất/nhỏ nhất | - | `np.argmax(dg)` → dùng để lấy tên sản phẩm đắt nhất |
| 17 | `NumPy` | `np.sum(arr)` | **Tổng** | $\sum x_i$ | `np.sum(sl * dg)` → Tổng giá trị tồn kho ~1.98 tỷ |
| 18 | `NumPy` | `np.dot(arr1, arr2)` | Tính **tổng tích** (Giá trị tồn kho = Tổng (Số lượng * Đơn giá)) | $\sum (sl_i \times dg_i)$ | `np.sum(sl * dg)` |
| 19 | `NumPy` | `np.corrcoef(arr1, arr2)` | **Hệ số tương quan Pearson** | $r$ | `np.corrcoef(sl, dg)[0,1]` → khoảng -0.3 |
| 20 | `NumPy` | `np.cov(arr1, arr2)` | **Hiệp phương sai** | $\text{cov}(X, Y) = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{n}$ | - |
| 21 | `NumPy` | `np.percentile(arr, q)` | **Phân vị** thứ q | - | `np.percentile(sl, 75)` → 135 cái |
| 22 | `NumPy` | `np.histogram(arr, bins)` | **Phân bố tần suất** | - | `np.histogram(sl, bins=5)` |
| 23 | `NumPy` | `np.where(condition)` | Trả về **index** thỏa điều kiện | - | `np.where(df['TenSP'].str.contains('Logitech'))` |
| 24 | `NumPy` | `np.sort(arr)` | **Sắp xếp** mảng | - | `np.sort(dg)` |
| 25 | `NumPy` | `np.average(arr, weights=w)` | **Trung bình có trọng số** | $\bar{x}_w = \frac{\sum (x_i \cdot w_i)}{\sum w_i}$ | `np.average(dg, weights=sl)` |
| 26 | `NumPy` | `np.logical_and(cond1, cond2)` | Kết hợp nhiều điều kiện | - | `np.logical_and(sl > 100, dg < 2000000)` |

