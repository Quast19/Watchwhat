from django.shortcuts import render
from watchwhat_app.models import Movie
from django.http import JsonResponse
def movie_list(request):
    movies = Movie.objects.all() #raw query set 
    data = {
        'movies': list(movies.values()) #converted data to list ie an interable format
    }
    
    return JsonResponse(data) #returned a Json format bro.