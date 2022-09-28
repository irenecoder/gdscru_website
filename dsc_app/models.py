from django.db import models
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    # resources = models.TextField(default=timezone.now)
    

    def __str__(self):
        return self.title

