from django.urls import path, include
from watchwhat_app.api.views import *
urlpatterns = [
    path('list/', MovieListAV.as_view(), name = 'movie-list'),
    path('list/<int:pk>', MovieDetailAV.as_view(), name = 'movie-details'),
]