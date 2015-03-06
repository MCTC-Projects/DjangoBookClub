from django.db import models




class User(models.Model):
    is_owner_user = models.BooleanField()
