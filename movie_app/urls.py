from django.urls import path
from movie_app import views

urlpatterns = [
    path('directors/', views.DirectorsListAPIView.as_view()),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('movies/', views.MovieListCreateAPIView.as_view()),
    path('movies/<int:id>', views.MovieDetailAPIView.as_view()),
    path('movies/reviews/', views.ReviewListCreateAPIView.as_view()),
    path('movies/reviews/<int:id>', views.ReviewDetailAPIView.as_view()),
]
