from django.db import models




'''BookClub is the main table. Everything is based off of what bookclub you are a part of'''
class BookClub(models.Model):
    bookclub_name = models.CharField(max_length=20)
    bookclub_description = models.TextField()
    owners_first_name = models.CharField(max_length=20)
    owners_email_address = models.EmailField()
    owners_password = models.CharField(max_length=30)

    def __str__(self):
        return str(self.bookclub_name)

'''A user can be in multiple bookclubs so User has a Many-to-Many relationship with BookClub'''
class User(models.Model):
    first_name = models.CharField(max_length=20)
    email_address = models.EmailField()
    password = models.CharField(max_length=15)
    bookclub = models.ManyToManyField(BookClub)

    def __str__(self):
        return str(self.first_name)+" Email: "+str(self.email_address)







'''A BookClub will have many books and a book might have many bookclubs so there is also a many-to-many relationship
between the two'''
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    isbn = models.IntegerField()
    description = models.TextField()
    bookclub = models.ForeignKey(BookClub)

    def __str__(self):
        return str(self.title) + " " +str(self.author)

'''Reviews will only have one book--you can not review multiple books with the same review-- so there is a Many-to-one relationship
between reviews and books'''
class Review(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return str(self.book)+" " + str(self.user)+ " "+ str(self.rating)