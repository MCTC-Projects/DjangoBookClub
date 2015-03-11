# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookclub',
            field=models.ManyToManyField(to='bookit.BookClub'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('book', 'user')]),
        ),
    ]
