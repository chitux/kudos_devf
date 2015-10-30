# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=320)),
                ('profile_picture', models.FileField(upload_to='')),
                ('phone', models.CharField(max_length=10)),
                ('kudollars', models.FloatField()),
                ('company_id', models.ForeignKey(to='company.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Kudo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kudo_body', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('employee_id', models.ForeignKey(to='employee.Employee')),
                ('writer', models.ForeignKey(related_name='writer', to='employee.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchase_date', models.TimeField(default=datetime.datetime.now)),
                ('status', models.BooleanField(default=True)),
                ('employee_id', models.ForeignKey(to='employee.Employee')),
                ('product_id', models.ForeignKey(to='company.Product')),
            ],
        ),
    ]
