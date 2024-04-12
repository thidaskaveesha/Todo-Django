from django.db import models

# Create your models here.
class TodoItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    