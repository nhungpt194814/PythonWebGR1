from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email', max_length=100)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    # widget dùng để che đi mật khẩu khi nhập
    password2 = forms.CharField(
        label='Password Again', widget=forms.PasswordInput())
    address = forms.CharField(label='Address')

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            # nếu true thì người dùng đã nhập pass1
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']

            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError('Invalid password')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Invalid username(special characters)')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Existed username')

    # hàm tạo tài khoản
    def save(self):
        User.objects.create_user(
            username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'], address=self.cleaned_data['address'])
