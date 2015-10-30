# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=320)),
                ('phone', models.CharField(max_length=10)),
                ('invitation_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=320)),
                ('price', models.FloatField(max_length=100)),
                ('icon', models.CharField(max_length=320)),
                ('company_id', models.ForeignKey(to='company.Company')),
            ],
        ),
    ]
