from django.contrib import admin
from first_app.models import Company, Employee, Detail, UserProfileInfo
# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Detail)
admin.site.register(UserProfileInfo)
