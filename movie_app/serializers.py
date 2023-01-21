from rest_framework import serializers

from movie_app.models import Director, Movie, Review


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id', 'name'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title', 'description', 'rating'


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    movie_reviews = ReviewDetailSerializer(many=True)


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

    directors_movie = MovieSerializer(many=True)
