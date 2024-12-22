# <center>Kiến trúc Hệ thống Web</center>

Tài liệu này cung cấp tổng quan về kiến trúc hệ thống web như được minh họa trong sơ đồ.

<center>
<img src="img/Architecture.jpg" width="auto" height="auto"/>
</center>

---

## 1. **Người dùng (Users)**
   - Người dùng tương tác với hệ thống để sử dụng các chức năng, bao gồm:
     - Phân tích dữ liệu khóa học.
     - Tìm kiếm khóa học theo tên.
     - Dự đoán mức độ hài lòng của một khóa học.
   - Người dùng thực hiện các thao tác như nhập thông tin, tra cứu dữ liệu và xem kết quả.

---

## 2. **Giao diện người dùng (Frontend)**
   - Hệ thống sử dụng **Streamlit** làm giao diện chính:
     - Streamlit đóng vai trò là cầu nối giữa người dùng và backend.
     - Cung cấp giao diện thân thiện, dễ sử dụng để hiển thị thông tin, kết quả phân tích hoặc dự đoán.
   - Frontend giao tiếp hai chiều với backend để gửi yêu cầu và nhận phản hồi.

---

## 3. **Backend**
   Backend bao gồm ba lớp chính:

   ### a. **Lớp Ứng dụng (Application Layer)**
   - Xử lý logic nghiệp vụ, bao gồm:
     - **Phân tích dữ liệu khóa học**: Xử lý và phân tích dữ liệu khóa học từ Lớp Dữ liệu.
     - **Tìm kiếm khóa học theo tên**: Cung cấp chức năng tìm kiếm thông minh dựa trên tên khóa học.
     - **Dự đoán mức độ hài lòng**: Sử dụng mô hình học máy để dự đoán mức độ hài lòng của học viên đối với khóa học.

   ### b. **Lớp Dữ liệu (Data Layer)**
   - Lưu trữ dữ liệu khóa học, bao gồm thông tin về khóa học, mức độ hài lòng và các thông tin liên quan khác.
   - Cung cấp dữ liệu cho Lớp Ứng dụng khi cần thiết.

   ### c. **Lớp Học máy (ML Layer)**
   - Bao gồm các **mô hình phân loại** được sử dụng để:
     - Phân loại và dự đoán mức độ hài lòng của học viên với khóa học.
     - Các mô hình được huấn luyện từ dữ liệu lưu trữ trong Lớp Dữ liệu.
   - Tích hợp với Lớp Ứng dụng để cung cấp kết quả dự đoán cho người dùng.

---

## Quy trình hoạt động tổng quát
1. Người dùng gửi yêu cầu từ giao diện Streamlit (ví dụ: phân tích hoặc tìm kiếm).
2. Yêu cầu được gửi đến Lớp Ứng dụng trong backend.
3. Lớp Ứng dụng xử lý yêu cầu, lấy dữ liệu từ Lớp Dữ liệu hoặc gọi Lớp Học máy để dự đoán.
4. Kết quả được trả về Frontend và hiển thị cho người dùng.

---
