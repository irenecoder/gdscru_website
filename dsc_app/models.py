from django.db import models
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    # url = models.URLField()
    # resources = models.TextField(default=timezone.now)
    

    def __str__(self):
        return self.title

