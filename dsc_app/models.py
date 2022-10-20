from django.db import models
from django.utils import timezone
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('dsc_app:event_detail',
        args=[self.published.year,
        self.published.month,
        self.published.day, self.slug])

