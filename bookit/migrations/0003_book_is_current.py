# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookit', '0002_bookclubmembers'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_current',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
