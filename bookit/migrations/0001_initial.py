# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('review', models.TextField()),
                ('rating', models.IntegerField()),
                ('book', models.ForeignKey(to='bookit.Book')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
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
