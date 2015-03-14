from django.contrib import admin
from bookit.models import Book,BookClub,Review,BookClubMembers

admin.site.register([Book,BookClub,Review,BookClubMembers])
