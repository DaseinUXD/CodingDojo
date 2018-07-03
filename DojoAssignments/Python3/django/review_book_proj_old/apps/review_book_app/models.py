from django.db import models
import re


# Create your models here.
# Our new manager!
# No methods in our new manager should ever catch the whole request object with a parameter!!!
# (just parts, like request.POST)
class UserManager(models.Manager):
    def basic_valildator(self, postData):
        errors ={}
        if len(postData['name']) < 2:
            errors['name'] = 'User name must be at least 2 characters in length'

        if len(postData['alias']) < 2:
            errors['alias'] = 'Alias must be at least 2 characters in length'

        if len(postData['email']) < 2:
            errors['name'] = 'User name must be at least 2 characters in length'

        if len(postData['password']) < 8:
            errors['password'] = 'Password  must be at least 8 characters in length'

        if len(postData['passworddd_confirm']) < 8:
            errors['password_confirm'] = 'Confirmation password does not equal password'

        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=20)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    book_reviews = models.ManyToManyField(User, through='Review')
    ranks = models.ManyToManyField(User, through='Review')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    user = models.ForeignKey(User, related_name='user_reviewed_books')
    book = models.ForeignKey(Book, related_name='books_reviewed_user')
    rank = models.ForeignKey(Book, related_name='books_ranks_user')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
