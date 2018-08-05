import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","part2.settings")

import django
django.setup()

from faker import Faker
from first_app.models import Company, Employee, Detail
import random
fakegen=Faker()


def populate(a=5,b=20):
    for i in range(a):
        fakecompany=fakegen.company()
        fakeurl=fakegen.url()
        create_company=Company.objects.get_or_create(company_name=fakecompany, url=fakeurl)[0]
        create_company.save()

    for i in range(b):
        company=Company.objects.get(id=random.randint(1,5))

        fakename=fakegen.name()
        fakejob=fakegen.job()
        create_employee=Employee.objects.get_or_create(company=create_company, employee_name=fakename, job=fakejob)[0]
        create_employee.save()

        fakephone=fakegen.msisdn()
        create_detail=Detail.objects.get_or_create(name=create_employee, phone=fakephone)[0]
        create_detail.save()

if __name__=='__main__':
    print('Populating')
    populate(5,20)
    print('Completed')
