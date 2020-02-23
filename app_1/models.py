from __future__ import unicode_literals
from django.db import models
import re



class UserManager(models.Manager):
    def register(self, postData):

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        PASSWORD_REGEX = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d,!@#$%^&*+=]{8,}$')

        errors = {}

        if len(postData['email']) < 2:
            errors['email'] = 'Email should be at least 2 characters!'
    
        if not EMAIL_REGEX.match(postData['email']):
            errors['email-invalid'] = 'Invalid Email!'

        check = User.objects.filter(email=postData['email'].lower())
        if len(check) > 0:
            errors['email-inuse'] = 'Email already in use!'

        if len(postData['password']) < 2:
            errors['password'] = 'Password should be at least 2 characters'
        elif not PASSWORD_REGEX.match(postData['password']):
            errors['password_valid'] = 'Password must contain at least 1 number and capitalization!'

        if len(postData['confirm_password']) < 1:
            errors['confirm_password'] = 'Confirm password is required!'
    
        elif postData['confirm_password'] != postData['password']:
            errors['confirm_password'] = 'Password must match Confirm password!'

        if User.objects.filter(email = postData['email']):
            errors["email_not_unique"] = "Provided email is already in use"
        
        return errors


    def login(self, postData):
        messages = []

        if len(postData['email']) < 1:
            messages.append('Email should be at least 2 characters!')

        if len(postData['password']) < 1:
            messages.append('Password should be at least 2 characters!')

        return messages



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f"<User object: {self.first_name},{self.last_name},{self.email}>"



class Message(models.Model):
    user_id = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Comment(models.Model):
    message_id = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
