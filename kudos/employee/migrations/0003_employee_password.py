# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20151030_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=40, default=datetime.datetime(2015, 11, 5, 0, 54, 44, 116438, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
