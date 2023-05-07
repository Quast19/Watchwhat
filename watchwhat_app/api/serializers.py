from rest_framework import serializers
from watchwhat_app.models import Watchwhat , StreamPlatform, Review 

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        exclude = ('watchwhat',)
        # fields = "__all__"

class WatchwhatSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many = True, read_only = True)
    
    # name_len = serializers.SerializerMethodField()
    class Meta:
        model = Watchwhat
        fields = "__all__"
    
    
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    
    # name_len_streamPlatform = serializers.SerializerMethodField()
    # 
    # Watchwhat = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='Watchwhat-details'
    # )
    url = serializers.HyperlinkedIdentityField(view_name="Watchwhat-details")
    watchwhat = WatchwhatSerializer(many = True , read_only = True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"

    # get_name_len_streamPlatform(self, )



    # def validate(self, data):
    #     if data['title']==data['description']:
    #         raise serializers.ValidationError("Name and Description must be different.")
    #     else:
    #         return data  
    
    # def validate_name(self, value):
    #     if len(value) <= 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value   
    
    


# def name_len(value):#core wala validator hai vai.
#     if len(value) <=2:
#         raise serializers.ValidationError("Name is too short")
#     else:
#         return value


# class WatchwhatSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(validators = [name_len])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
    
#     def create(self, validated_data):
#         return Watchwhat.objects.create(**validated_data)# we could just written Watchwhat.objects.create(**validated_data), and not return it, but we need to display the data so we wrote the other way.
    
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