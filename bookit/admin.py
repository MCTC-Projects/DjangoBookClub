from django.contrib import admin
from bookit.models import Book,BookClub,Review,User


admin.site.register([Book,BookClub,Review,User])
