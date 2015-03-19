from django.db import models
from django.contrib.auth.models import User



'''BookClub is the main table. Everything is based off of what bookclub you are a part of'''
class BookClub(models.Model):
    bookclub_name = models.CharField(max_length=20)
    bookclub_description = models.TextField()
    owner = models.OneToOneField(User)

    def natural_key(self):
        return (self.bookclub_name,)

    def __str__(self):
        return str(self.bookclub_name)


'''Users can be in Many BookClubs and BookClubs have many Users'''
class BookClubMembers(models.Model):
    user = models.ManyToManyField(User)
    bookclub = models.OneToOneField(BookClub)





'''A BookClub will have many books so there is a one-to-many relationship
between the two'''
class Book(models.Model):
    is_current = models.BooleanField(default=False)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    isbn = models.IntegerField()
    description = models.TextField()
    bookclub = models.ForeignKey(BookClub)

    def __str__(self):
        return str(self.title) + " " +str(self.author)

'''Reviews will only have one book--you can not review multiple books with the same review-- so there is a Many-to-one relationship
between reviews and books and a many-to-one relationship between reviews and Users'''
class Review(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    review = models.TextField()
    rating = models.IntegerField()

    class Meta:
        unique_together = (('book','user'),)

    def __str__(self):
        return str(self.book)+" " + str(self.user)+ " "+ str(self.rating)