from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from django.views.generic import ListView
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return render(request, 'pages/home.html')
    # hàm index sẽ vào pages/home.html


def contact(request):
    return render(request, 'pages/contact.html')


def error(request, *args, **kwargs):
    return render(request, 'pages/error.html')


def register(request):
    # tạo form
    form = RegistrationForm()
    if request.method == 'POST':
        # đưa dữ liệu người dùng nhập vào form
        form = RegistrationForm(request.POST)
        # kiểm tra xem dữ liệu có hợp lệ không, với các hàm clean_
        if form.is_valid():
            # nếu hợp lệ thì save
            form.save()
            # khi đăng nhập thành công thì đưa nó tới đường dẫn về trang chủ
            return HttpResponseRedirect('/')

    # nếu method là GET thì hiển thị form
    return render(request, 'pages/register.html', {'form': form})


def user_list(request):
    return render(request, 'pages/user_list.html')


class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'pages/user_list.html'
    context_object_name = 'Users'
    paginate_by = 10  # maximum per page is 1 blog posts
