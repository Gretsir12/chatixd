from django.db import models

# Create your models here.
class UserContact(models.Model): #user contact model
    contact_username = models.CharField(max_length=50)
    owner_username = models.CharField(max_length=50)

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, null=True)
    chats = models.ManyToManyField(UserContact, blank=True, null=True) 
    def __str__(self):
        return self.username