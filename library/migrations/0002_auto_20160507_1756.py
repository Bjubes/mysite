# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 21:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='title',
            new_name='name',
        ),
    ]