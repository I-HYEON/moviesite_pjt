from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField(default=None)
    release_date = models.DateField(default=None)
    genre = models.CharField(max_length=30,default=None)
    score = models.FloatField(default=None)
    poster_url = models.CharField(max_length=50,default=None)
    description = models.TextField()
    actor_image = models.ImageField(blank=True,null=True,default='default_actor_image.png')
