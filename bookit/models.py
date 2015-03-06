from django.db import models



'''A user can be in multiple bookclubs so User has a Many-to-Many relationship with BookClub'''
class User(models.Model):
    first_name = models.CharField()
    email_address = models.EmailField()
    password = models.CharField()
    bookclub = models.ManyToManyField(BookClub)





'''BookClub is the main table. Everything is based off of what bookclub you are a part of'''
class BookClub(models.Model):
    bookclub_name = models.CharField()
    bookclub_description = models.TextField()
    owners_first_name = models.CharField()
    owners_email_address = models.EmailField()
    owners_password = models.CharField()




'''A BookClub will have many books and a book might have many bookclubs so there is also a many-to-many relationship
between the two'''
class Book(models.Model):
    title = models.CharField()
    author = models.CharField()
    isbn = models.IntegerField()
    description = models.TextField()
    bookclub = models.ManyToManyField(BookClub)


'''Reviews will only have one book--you can not review multiple books with the same review-- so there is a Many-to-one relationship
between reviews and books'''
class Review(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    review = models.TextField()
    rating = models.IntegerField()