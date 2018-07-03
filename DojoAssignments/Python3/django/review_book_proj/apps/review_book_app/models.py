from django.db import models
import re

# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def register(self, request):
        errors = {}
        if User.objects.filter(email=request['email']).exists():
            errors['exists'] = "This email address already exists in the database"
            print(errors)
            return errors
        else:
            if len(request['name']) < 2:
                errors['name'] = "Name must be longer than two characters"
                # return errors

            if len(request['alias']) < 2:
                errors['alias'] = "Alias must be longer than two characters"
                # return errors

            if not EMAIL_REGEX.match(request['email']):
                errors['email'] = "Must enter a valid email"
                # return errors

            if len(request['password']) < 8:
                errors['password'] = "Password must be at least 8 characters"
                # return errors

            if not request['password_confirm'] == request['password']:
                errors['password_confirm'] = "Passwords do not match"
                # return errors

            return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


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
