from django.db import models
from datetime import datetime


class Employee(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(max_length=320)
    profile_picture = models.FileField(upload_to='profile_pictures')
    phone = models.CharField(max_length=10)
    kudollars = models.FloatField(default=0.0)
    company_id = models.ForeignKey('company.Company')
    password = models.CharField(max_length=40)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Kudo(models.Model):
    writer = models.ForeignKey('employee.Employee', related_name='writer')
    employee_id = models.ForeignKey('employee.Employee')
    kudo_body = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


class Purchase(models.Model):
    product_id = models.ForeignKey('company.Product')
    employee_id = models.ForeignKey('employee.Employee')
    purchase_date = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=True)
