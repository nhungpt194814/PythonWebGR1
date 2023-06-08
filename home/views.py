from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import RegistrationForm, LoginForm
from django.views.generic import ListView
from django.contrib.auth import get_user_model, authenticate, login
from .models import User
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


def user_login(request):
    error_message = None  # Thêm giá trị mặc định cho error_message
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # Đổi 'home' thành tên URL của trang chủ
                return redirect('pages/home')
        else:
            error_message = 'Invalid email or password.'
            return render(request, 'pages/login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form, 'error_message': error_message})


class UserListView(ListView):
    model = User
    queryset = get_user_model().objects.all()
    template_name = 'pages/user_list.html'
    context_object_name = 'Users'
    paginate_by = 10  # maximum per page is 1 blog posts
