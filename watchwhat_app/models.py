from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=30)
    description  = models.TextField(max_length=200)
    active = models.BooleanField(default=True)#by default we expect that the movie is released, if active==false, the movie is not released yet
    
    def __str__(self):
        return self.name