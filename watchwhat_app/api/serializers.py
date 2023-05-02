from rest_framework import serializers
from watchwhat_app.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)# we could just written Movie.objects.create(**validated_data), and not return it, but we need to display the data so we wrote the other way.
    
    def update(self,instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        return instance