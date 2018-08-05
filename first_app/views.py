from django.shortcuts import render
from first_app.models import Company, Employee, Detail
from first_app.forms import EmployeeForm, DetailForm, UserForm, UserProfileForm
from django import forms

from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'first_app/home.html', {'context_dict':'test filter'})

def index(request):
    emp_phones=Detail.objects.order_by('id')
    context_dict={'emp_phones':emp_phones}
    return render(request, 'first_app/index.html', context=context_dict)

def form(request):
    employee_form=EmployeeForm()
    # detail_form=DetailForm()
    if request.method=='POST':
        employee_form=EmployeeForm(request.POST)
        detail_form=DetailForm(request.POST)
        if employee_form.is_valid():
            employee_form.save()
            return home(request)
        else:
            print('EHHHHHHHHHHHHHHHH')
    return render(request, 'first_app/forms.html', {'employee_form':employee_form})

def register(request):
    registered=False
    if request.method== 'POST':
        user_form=UserForm(data=request.POST)
        user_profile_form=UserProfileForm(data=request.POST)
        if user_form.is_valid() and user_profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=user_profile_form.save(commit=False)
            profile.user=user
            if 'user_pic' in request.FILES:
                profile.user_pic=request.FILES['user_pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors,user_profile_form.errors)
    else:
        user_form=UserForm()
        user_profile_form=UserProfileForm()
    return render(request, 'first_app/register.html',{'user_form':user_form,
                                                        'user_profile_form':user_profile_form,
                                                        'registered':registered})

def user_login(request):
    if request.method=='POST':
        id=request.POST.get('id')
        password=request.POST.get('password')
        user=authenticate(request, username=id, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(id,password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'first_app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
