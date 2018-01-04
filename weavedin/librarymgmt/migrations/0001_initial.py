# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
    ]
