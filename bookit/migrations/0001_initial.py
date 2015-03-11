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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=20)),
                ('isbn', models.IntegerField()),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookClub',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('bookclub_name', models.CharField(max_length=20)),
                ('bookclub_description', models.TextField()),
                ('owners_first_name', models.CharField(max_length=20)),
                ('owners_email_address', models.EmailField(max_length=75)),
                ('owners_password', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('review', models.TextField()),
                ('rating', models.IntegerField()),
                ('book', models.ForeignKey(to='bookit.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=15)),
                ('bookclub', models.ManyToManyField(to='bookit.BookClub')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(to='bookit.User'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('book', 'user')]),
        ),
        migrations.AddField(
            model_name='book',
            name='bookclub',
            field=models.ManyToManyField(to='bookit.BookClub'),
            preserve_default=True,
        ),
    ]
