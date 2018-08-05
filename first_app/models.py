from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
    company_name=models.CharField(max_length=50)
    url=models.CharField(max_length=50)


    def __str__(self):
        return self.company_name

class Employee(models.Model):
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_name=models.CharField(max_length=50)
    job=models.CharField(max_length=50)


    def __str__(self):
        return self.employee_name

class Detail(models.Model):
    name=models.ForeignKey(Employee, on_delete=models.CASCADE)
    phone=models.IntegerField()

    def __str__(self):
        return str(self.phone)

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    user_url=models.URLField(max_length=50, blank=True)
    user_pic=models.ImageField(upload_to= 'profile_pics', blank=True)
    def __str__(self):
        return self.user.username
