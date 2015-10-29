from django.db import models
from datetime import datetime


class Employee(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(max_length=320)
    profile_picture = models.FileField()
    phone = models.CharField(max_length=10)
    kudollars = models.FloatField()
    company_id = models.ForeignKey('company.Company')


class Kudo(models.Model):
    writer = models.ForeignKey('employee.Employee')
    employee_id = models.ForeignKey('employee.Employee')
    kudo_body = models.char(255)
    is_active = models.BooleanField(defaul=True)


class Purchase(models.Model):
    product_id = models.ForeignKey('company.Product')
    employee_id = models.ForeignKey('employee.Employee')
    purchase_date = models.TimeField(default=datetime.now)
    status = models.BooleanField(default=True)
