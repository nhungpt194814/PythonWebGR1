from django.test import TestCase, SimpleTestCase
# câu lệnh chạy tất cả các file test: python3 manage.py test
# Create your tests here.

# viết các test case để tự test


class SimpleTest(SimpleTestCase):
    # write class SimpleTest, which is a subclass of SimpleTestCase

    def test_home_page_status(self):
        response = self.client.get('/')
        # khi client get đường dẫn trên, nó sẽ thực hiện hàm index và trả về respone
        # nếu thành công trả về 200
        # nếu không thành công trả về 404
        self.assertEquals(response.status_code, 200)
        # nếu trả về equal với 200 thì trả về ok, không thì fail
