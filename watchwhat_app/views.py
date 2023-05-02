# from django.shortcuts import render
# from watchwhat_app.models import Movie
# from django.http import JsonResponse
# from django.http import HttpResponse
# def movie_list(request):
#     movies = Movie.objects.all()#raw query set 
#     movies_list = list(movies.values())#iterable python from raw query set.
#     data = {
#         'movies': movies_list#converted data to list ie an interable format
#     }
    
#     return JsonResponse(data) #returned a Json format bro.


# def movie_details(request, pk): #this one gives a specific movie wrt the primary key
#     the_movie = Movie.objects.get(pk = pk)
#     print(the_movie)
#     data = {
#         'name' : the_movie.name,
#         'description' : the_movie.description,
#         'active' : the_movie.active,
#     }
#     return JsonResponse(data)