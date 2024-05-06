from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Movie
from PIL import Image
from .serializers import *
from .models import *
import traceback

# Create your views here.
class UserSignUpAPIView(APIView):
    def post(self,request):
        user_serializer = UserSignUpSerializer(data = request.data)
        try:
            if user_serializer.is_valid():
                user = user_serializer.save()
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token
                resp_data ={
                    "user":user_serializer.data,
                    "access_token":str(access_token)
                }
                return Response({"data":resp_data})
            return Response({"err":user_serializer.errors})
        
        except :
            traceback.print_exc()
            return Response({"Err":"something wrong"})


# moview
class MovieViewSet(viewsets.ModelViewSet):
    
    queryset = Movie.objects.all()
    qqueryset = Movie.objects.all().values('user_rating')
    print("q",qqueryset)

    serializer_class = MovieSerializer




# rating 
class MovieRatingAPIView(APIView):
    def post(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            user = request.user
            rating_value = request.data.get('rating')
            if not rating_value:
                return Response({"error": "Rating is required."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Check if the user has already rated the movie
            existing_rating = MovieRating.objects.filter(movie=movie, user=user).first()
            if existing_rating:
                existing_rating.rating = rating_value
                existing_rating.save()
                serializer = MovieRatingSerializer(existing_rating)
                return Response(serializer.data)
            else:
                rating_instance = MovieRating.objects.create(movie=movie, user=user, rating=rating_value)
                serializer = MovieRatingSerializer(rating_instance)
                return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)



# movie listing 
def movie_listing_view(request):
    movies = Movie.objects.all()  
    for movie in movies:
        img_path = movie.img_path.path  
        with Image.open(img_path) as img:
            movie.width, movie.height = img.size
    return render(request, 'movie_listing.html', {'movies': movies})


# movies detail
def movie_detail_view(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})






















