from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here. This model was just for explaining crud operations and a lot of things now we re model the django project
# class Movie(models.Model):
#     name = models.CharField(max_length=30)
#     description  = models.TextField(max_length=200)
#     active = models.BooleanField(default=True)#by default we expect that the movie is released, if active==false, the movie is not released yet
    
#     def __str__(self):
#         return self.name

class StreamPlatform(models.Model):
   
    
    name = models.CharField(max_length = 30)
    about = models.CharField(max_length = 190)
    website = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class Watchwhat(models.Model):
    title = models.CharField(max_length=90)
    description  = models.TextField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add= True)
    platform = models.ForeignKey(StreamPlatform,null=True, on_delete=models.CASCADE, related_name = "Watchwhat")
    average_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
    

    
    
class Review(models.Model):
    review_user =  models.ForeignKey(User, on_delete= models.CASCADE)
    rating = models.PositiveIntegerField(validators = [MinValueValidator(1),MaxValueValidator(5)])
    watchwhat = models.ForeignKey(Watchwhat, on_delete=models.CASCADE, related_name = "reviews")
    description = models.CharField(max_length = 200, null = True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now =True)
    active = models.BooleanField(default=True)  

    def __str__(self):
        return "Rating : " + str(self.rating) + ", " + self.watchwhat.title