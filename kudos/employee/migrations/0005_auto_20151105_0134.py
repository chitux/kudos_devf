# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20151105_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='kudollars',
            field=models.FloatField(default=0.0),
        ),
    ]
