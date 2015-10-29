from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=320, uniq=True)
    phone = models.CharField(max_length=10)
    invitation_code = models.CharField(max_length=10)


class Product(models.Model):
    company_id = models.ForeingKey(Company)
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=320)
    price = models.FloatField(max_length=100)
    icon = models.FileField(max_length=10)

