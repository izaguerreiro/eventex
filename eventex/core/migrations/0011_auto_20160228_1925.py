# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-28 19:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_course_abc_to_mti'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseold',
            name='speakers',
        ),
        migrations.DeleteModel(
            name='CourseOld',
        ),
    ]
