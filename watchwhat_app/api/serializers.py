from rest_framework import serializers
from watchwhat_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = "__all__"
    
    def validate(self, data):
        if data['name']==data['description']:
            raise serializers.ValidationError("Name and Description must be different.")
        else:
            return data  
    
    def validate_name(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value   
    
    


# def name_len(value):#core wala validator hai vai.
#     if len(value) <=2:
#         raise serializers.ValidationError("Name is too short")
#     else:
#         return value


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(validators = [name_len])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)# we could just written Movie.objects.create(**validated_data), and not return it, but we need to display the data so we wrote the other way.
    
#     def update(self,instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         return instance
    
#     def validate(self, data):
#         if data['name']==data['description']:
#             raise serializers.ValidationError("Name and Description must be different.")
#         else:
#             return data
    
#     # def validate_name(self, value):
#     #     if len(value) <= 2:
#     #         raise serializers.ValidationError("Name is too short")
#     #     else:
#     #         return value   