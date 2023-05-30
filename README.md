
<a name="readme-top"></a>

<br />
<div align="center">
  <h3 align="center">Python Web</h3>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#About-Django">About Django</a>
      <ul>
        <li><a href="#Django-la-gi">Django là gì?</a></li>
        <li><a href="#Lịch-sử-của-Django ">Lịch sử của Django</a></li>
        <li><a href="#Tại-sao-nên-dùng-Django?">Tại sao nên dùng Django?</a></li>
        <li><a href="#Ưu-điểm-của-Django">Ưu điểm của Django</a></li>
        <li><a href="#Nhược-điểm-của-Django">Nhược điểm của Django</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About Django
### Django la gi
* Django là một web framework bậc cao, miễn phí, sử dụng mã nguồn mở 
* Lập trình bằng ngôn ngữ python 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Lịch sử của Django 
* Django được bắt đầu bởi Adrian Holovaty, Simon Willision vào năm 2003 
* Lý do nó được sinh ra bởi vì 2 chú này đều chán ngấy với việc duy trì các trang web lớn bằng PHP( tại thời điểm đó PHP có nhiều vấn đề như: quản lý mã nguồn không có tổ chức, khó bảo trì, khó hiểu, các vấn đề bảo mật,...) và cả 2 đều thích Python cho nên cả 2 muốn chuyển qua phát triển web bằng Python. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Tại sao nên dùng Django? 
* Nhanh chóng và đơn giản: mục tiêu của Django là đơn giản hóa công việc cho lập trình viên, nên để làm vậy, Django framework sử dụng nguyên tắc phát triển nhanh chóng (có thể thực hiện nhiều iteration cùng 1 lúc) và Don’t Repeat Yourself (lập trình viên có thể tái sử dụng những đoạn code đã tồn tại và tập trung vào các điểm unique). 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Ưu điểm của Django: 

* Cấu trúc phát triển mạnh mẽ: cho phép tổ chức, quản lý mã nguồn hiệu quả, dễ bảo trì, mở rộng 
* Tích hợp đầy đủ các tính năng phổ biến trong ứng dụng web giúp giảm thời gian phát triển
* Mô hình MVC: dễ phát triển, bảo trì, mở rộng, kiểm thử 
* Bảo mật cao  

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Nhược điểm của Django: 

* Framework có nhiều tính năng mạnh, không cần thiết để sử dụng cho các ứng dụng nhỏ
* Khả năng tùy chỉnh hạn chế
* Không hiệu quả khi xử lý các ứng dụng web có lưu lượng truy cập lớn, tốc độ xử lý cao

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Structure of a Django application
The structure of a typical Django application consists of the following components:

* `models.py`: Nơi định nghĩa các models cho ứng dụng. Models mô tả cấu trúc dữ liệu của các đối tượng trong ứng dụng và được sử dụng để tương tác với cơ sở dữ liệu.
* `views.py`: Nơi chứa các hàm hoặc các lớp để xử lý yêu cầu từ người dùng và trả về các phản hồi tương ứng.
* `urls.py`: Nơi chứa các mẫu URL (url patterns) cho ứng dụng. Mỗi url pattern định nghĩa đường dẫn và liên kết nó với một hàm xử lý yêu cầu trong `views.py`.
* `forms.py` (tùy chọn): Nơi định nghĩa các form để xử lý dữ liệu người dùng. Form giúp xác thực và xử lý dữ liệu nhập vào từ người dùng trước khi lưu vào cơ sở dữ liệu.
* `templates`: Thư mục chứa các mẫu templates cho giao diện người dùng
* `static`: Thư mục để lưu trữ các tệp tĩnh(static) như CSS, JavaScript hoặc hình ảnh. Các tệp tĩnh này có thể được sử dụng trong giao diện người dùng.

## MVC architecture in Django
Django sử dụng mô hình kiến trúc MVC(Model-View-Controller) trong việc phát triển ứng dụng web. Tuy nhiên, Django đặt tên các thành phần theo cấu trúc MVT(Model-View-Template).
1. Model:
* Model trong Django đại diện cho cấu trúc dữ liệu của ứng dụng, dùng để mô tả các đối tượng và mối quan hệ giữa chúng. Model định nghĩa các trường và các phương thức để tương tác với cơ sở dữ liệu.
* `models.py` chứa các lớp mô hình. Mỗi lớp đại diện cho một bảng trong cơ sở dữ liệu và sử dụng các trường để định nghĩa cấu trúc dữ liệu.

2. View:
* Trong Django, view là nơi xử lý logic và tương tác với model và yêu cầu từ người dùng(thay thế Controller). View không chỉ dùng để trình diễn dữ liệu mà còn có thể xử lý yêu cầu HTTP và trả về phản hồi tương tự.
* `views.py` chứa các hàm hoặc các lớp, nó nhận yêu cầu từ người dùng, tương tác với cơ sở dữ liệu và trả về phản hồi.

3. Template:
* Template dùng để định nghĩa giao diện người dùng, dùng để hiển thị dữ liệu từ models và các phản hồi từ view.

<!-- GETTING STARTED -->
## Getting Started

### Installation
How to install and set up on WSL
1. Install django and gunicorn with `pip install gunicorn django`

<!-- CONTACT -->
## Contact

Anh Nhung - [@GitHub](https://github.com/nhungpt194814) - nhung.pt194814@gmail.com

Project Link: [https://github.com/nhungpt194814/PythonWebGR1](https://github.com/nhungpt194814/PythonWebGR1)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best README Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md?plain=1)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
