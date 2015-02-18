# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_topmenu'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
