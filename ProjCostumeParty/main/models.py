from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=350)
    slug = models.SlugField(max_length=350,unique_for_date='publish')
    description = models.TextField(default='Hello World')
    location = models.CharField(max_length=250,default='Bangalore')
    images = models.ImageField(upload_to='uploads/')
    publish = models.DateTimeField(default=timezone.now)
    all_posts = models.Manager() #default manager.

class Meta:
    ordering = ('-publish',)

def __str__(self):
    self.title
