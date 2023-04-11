from django.db import models
from django.conf import settings

# Create your models here.

class Movie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    audience = models.IntegerField(default=None)
    release_date = models.DateField(default=None)
    genre = models.CharField(max_length=30,default=None)
    score = models.FloatField(default=None)
    poster_url = models.CharField(max_length=50,default=None)
    description = models.TextField()
    actor_image = models.ImageField(blank=True,null=True,default='default_actor_image.png')

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='comments')
    content = models.CharField(max_length=140,help_text='최대 140자 이내로 작성하세요',verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
