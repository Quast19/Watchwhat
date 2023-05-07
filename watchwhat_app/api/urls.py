from django.urls import path, include
from watchwhat_app.api.views import *
urlpatterns = [
    path('list/', WatchwhatListAV.as_view(), name = 'Watchwhat-list'),
    path('list/<int:pk>', WatchwhatDetailAV.as_view(), name = 'Watchwhat-detail'),
    path('stream/<int:pk>',  StreamPlatformDetailAV.as_view(), name = 'platform-detail'),
    path('stream/',StreamPlatformAV.as_view(), name ='stream-list'),
    
    
    # path('review/',ReviewList.as_view(), name ='review-list'),
    # path('review/<int:pk>',ReviewDetail.as_view(), name ='review-list')
    
    path('stream/<int:pk>/review-create/',ReviewCreate.as_view(), name ='review-list'),
    path('stream/<int:pk>/review/',ReviewList.as_view(), name ='review-create'),
    path('stream/review/<int:pk>/',ReviewDetail.as_view(), name ='review-list'),
]