from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm, LoginForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import User


def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            login(request, user)
            # return redirect('home')  # Đổi 'home' thành tên URL của trang chủ
            return HttpResponseRedirect('/')

    else:
        form = SignupForm()
    return render(request, 'pages/register.html', {'form': form})


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 # Đổi 'home' thành tên URL của trang chủ
#                 # return redirect('home')
#                 return HttpResponseRedirect('/')

#     else:
#         form = LoginForm()
#     return render(request, 'pages/login.html', {'form': form})

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
                return redirect('http://localhost:8000/blog/')
        else:
            error_message = 'Invalid email or password.'
            return render(request, 'pages/login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form, 'error_message': error_message})


class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'pages/user_list.html'
    context_object_name = 'Users'
    paginate_by = 10  # maximum per page is 1 blog posts
