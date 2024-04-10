from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.TextField()
    description = models.TextField()
    
