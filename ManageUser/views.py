from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm, LoginForm
from django.http import HttpResponseRedirect


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


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Đổi 'home' thành tên URL của trang chủ
                # return redirect('home')
                return HttpResponseRedirect('/')

    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form})
