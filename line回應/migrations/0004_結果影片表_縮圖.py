# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('line回應', '0003_結果影片表'),
    ]

    operations = [
        migrations.AddField(
            model_name='結果影片表',
            name='縮圖',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
