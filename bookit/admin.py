from django.contrib import admin
from bookit.models import Book,BookClub,Review

admin.site.register([Book,BookClub,Review])
