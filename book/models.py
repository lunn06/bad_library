from django.db import models
from django.conf import settings
from django.utils import timezone


class Author(models.Model):
    name = models.TextField()
    description = models.TextField()
    books = models.ManyToManyField('Book', blank=True)
    birthday = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "author"
    
    def __str__(self):
        return self.name
    
        
class Genre(models.Model):
    name = models.TextField()
    description = models.TextField()
    books = models.ManyToManyField('Book', blank=True)

    class Meta:
        db_table = "genre"
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    uri = models.TextField()
    publication_date = models.DateField(default=timezone.now)
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    content = models.TextField(blank=True, null=True)
    rating = models.SmallIntegerField()

    class Meta:
        db_table = 'review'
    

