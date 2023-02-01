from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1)
    description = serializers.CharField(min_length=1)
    duration = serializers.IntegerField(default=0)
    director_id = serializers.IntegerField(min_value=1)


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1)


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=10, required=True)
    stars = serializers.IntegerField(min_value=1, max_value=5, required=True)
    movie_id = serializers.IntegerField(min_value=1, required=True)

    def validate_movie_id(self, movie_id):
        movie_exists = Movie.objects.filter(id=movie_id).exists()
        if movie_exists:
            return movie_id
        raise ValidationError('Фильма с таким id не существует')


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

    directors_movie = MovieSerializer(many=True)
