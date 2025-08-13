from operator import length_hint
from django.db import models

# Create your models here.
    
class Message(models.Model): #message model
    sender_username = models.CharField(max_length=50, null=True)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)