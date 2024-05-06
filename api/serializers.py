from rest_framework import serializers
from django.db.models import Avg
from .models import *



class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','first_name','last_name','username','email','password')


    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



# movie serilaizer
class MovieSerializer(serializers.ModelSerializer):
    user_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'
    

    def get_user_rating(self, obj):
        average_rating = obj.ratings.aggregate(Avg('rating'))['rating__avg']
        return average_rating if average_rating is not None else 0

    def to_representation(self, instance):
        average_rating = instance.ratings.aggregate(Avg('rating'))['rating__avg']
        instance.user_rating = average_rating if average_rating is not None else 0
        instance.save()
        representation = super().to_representation(instance)
        # Manually reorder the fields
        fields_order = ['id', 'name', 'description', 'img_path', 'duration', 'genre', 'language', 'mpaa_Rating', 'user_rating', 'created_at', 'updated_at']
        ordered_representation = {key: representation[key] for key in fields_order}
        return ordered_representation


# rating
class MovieRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRating
        fields = ('id', 'movie', 'user', 'rating', 'created_at')














