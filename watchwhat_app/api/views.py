from watchwhat_app.models import Watchwhat,StreamPlatform, Review
from watchwhat_app.api.serializers import WatchwhatSerializer,StreamPlatformSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = Watchwhat.objects.get(pk=pk)
        serializer.save(watchwhat = movie)
        
class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchwhat = pk)
    

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class StreamPlatformAV(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many = True, context={'request': request} )
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors )
        
        
class StreamPlatformDetailAV(APIView):
            
    def get(self,request,pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({
                'Watchwhat not found'
            },status = status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform,context={'request': request})
        return Response(serializer.data)
    
    def put(self, request,pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({
                'Watchwhat not found'
            },status = status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
        
        
    def delete(self, request,pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({
                'Watchwhat not found'
            },status = status.HTTP_404_NOT_FOUND)
        platform.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class WatchwhatListAV(APIView):
    def get(self,request):
        Watchwhats =Watchwhat.objects.all()
        serializer = WatchwhatSerializer(Watchwhats,many= True, )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchwhatSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class WatchwhatDetailAV(APIView):
    
    def get(self,request,pk):
        try:
            watchwhat = Watchwhat.objects.get(pk=pk)
        except Watchwhat.DoesNotExist:
            return Response({
                'Watchwhat not found'
            },status = status.HTTP_404_NOT_FOUND)
        serializer = WatchwhatSerializer(watchwhat)
        return Response(serializer.data)
    
    def put(self, request,pk):
        try:
            watchwhat = Watchwhat.objects.get(pk=pk)
        except Watchwhat.DoesNotExist:
            return Response({
                'Watchwhat not found'
            },status = status.HTTP_404_NOT_FOUND)
        serializer = WatchwhatSerializer(watchwhat, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
        
        
    def delete(self, request,pk):
        try:
            Watchwhat = Watchwhat.objects.get(pk=pk)
        except Watchwhat.DoesNotExist:
            return Response({
                'Watchwhat not found'
            },status = status.HTTP_404_NOT_FOUND)
        Watchwhat.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)#coz after deleting we have no content on that page anymore.
    
# @api_view(['GET','POST'])
# def Watchwhat_list(request):
#     if request.method == 'GET':
#         Watchwhats = Watchwhat.objects.all()
#         serializer = WatchwhatSerializer(Watchwhats,many = True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = WatchwhatSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else :
#             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT', 'DELETE'])
# def Watchwhat_details(request, pk):
#     try:
#         Watchwhat = Watchwhat.objects.get(pk=pk)
#     except Watchwhat.DoesNotExist:
#         return Response({
#             'Watchwhat not found'
#         },status = status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = WatchwhatSerializer(Watchwhat)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = WatchwhatSerializer(Watchwhat, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else :
#             return Response(serializer.errors)
        
        
#     if request.method == 'DELETE':
#         Watchwhat.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)#coz after deleting we have no content on that page anymore.
        
