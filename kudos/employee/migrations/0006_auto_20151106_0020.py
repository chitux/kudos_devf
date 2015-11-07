# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20151105_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_picture',
            field=models.FileField(upload_to='profile_pictures'),
        ),
    ]
