from django.db import models


class Director(models.Model):
    name = models.CharField(verbose_name='Режиссер', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Режиссёр"
        verbose_name_plural = "Режиссёры"


class Movie(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    duration = models.IntegerField(verbose_name='Продолжительность в минутах', blank=True, null=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, verbose_name='Режиссер', null=True, 
                                 related_name='directors_movie')

    @property
    def rating(self):
        rate = self.movie_reviews.count()
        if rate == 0:
            return 0
        avr = 0
        for i in self.movie_reviews.all():
            avr += i.stars
        return avr / rate

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Review(models.Model):
    text = models.TextField(verbose_name='Текст', null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='К фильму', related_name='movie_reviews')
    stars = models.IntegerField(choices=CHOICES, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
