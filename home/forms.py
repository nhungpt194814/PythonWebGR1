from django import forms
import re
from .models import User
from django.core.exceptions import ObjectDoesNotExist


class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    # widget dùng để che đi mật khẩu khi nhập
    password2 = forms.CharField(
        label='Password Again', widget=forms.PasswordInput())
    mobile = forms.CharField(label='Mobile', max_length=50)
    address = forms.CharField(label='Address')

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            # nếu true thì người dùng đã nhập pass1
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']

            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError('Invalid password')

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if not re.search(r'^\w+$', username):
    #         raise forms.ValidationError('Invalid username(special characters)')
    #     try:
    #         User.objects.get(username=username)
    #     except ObjectDoesNotExist:
    #         return username
    #     raise forms.ValidationError('Existed username')

    # hàm tạo tài khoản
    def save(self):
        User.objects.create_user(
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            mobile=self.cleaned_data['mobile'],
            password=self.cleaned_data['password1'],
            address=self.cleaned_data['address'])


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
