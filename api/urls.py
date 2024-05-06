from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('',MovieViewSet,basename='movies')



urlpatterns = [
    path('movie/', include(router.urls)),
    path('movies/<int:movie_id>/rate/', MovieRatingAPIView.as_view(), name='movie-rate'),
    path('movies/', movie_listing_view, name='movie_listing'),
    path('movies/<int:movie_id>/', movie_detail_view, name='movie_detail'),


]