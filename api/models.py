from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(blank=True, null=True, max_length=100)
    last_name = models.CharField(blank=True, null=True, max_length=100)
    username = models.CharField(blank=True, null=True, max_length=16)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']



# For movie
class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    img_path = models.ImageField()
    duration = models.IntegerField()
    genre = models.TextField(blank=True,null=True)
    language = models.CharField(max_length=50)
    mpaa_Rating = models.JSONField() 
    user_rating = models.DecimalField(blank=True,null=True,max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_genre(self, genre_list):
        self.genre = ', '.join(genre_list)

    def get_genre(self):
        return [genre.strip() for genre in self.genre.split(',')]

    def __str__(self):
        return self.name


# rating moview
class MovieRating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    