from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    list_display = ("title", "duration")



admin.site.register(Director)
admin.site.register(Review)
