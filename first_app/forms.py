from django import forms
from django.core import validators
from first_app.models import Company, Employee, Detail, UserProfileInfo
from django.contrib.auth.models import User


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class DetailForm(forms.ModelForm):
    class Meta:
        model=Detail
        fields= ['phone']

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields=('user_url','user_pic')
