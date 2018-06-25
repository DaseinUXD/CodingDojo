from django.db import models
import re

# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')




class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    book_reviews = models.ManyToManyField(User, related_name='user_book_reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



class Review(models.Model):
    reviewer = models.ForeignKey(User, related_name='user_review')
    book = models.ForeignKey(Book, related_name='review_of_book')
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

