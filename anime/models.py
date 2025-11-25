from django.db import models
from .choices import AnimeStatus


class Studio(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Anime(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    cover_image = models.ImageField(upload_to='anime_covers/', blank=True)
    status = models.CharField(max_length=20, choices=AnimeStatus.choices, default=AnimeStatus.ANNOUNCED.value)
    release_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    # Relationships
    studio = models.ForeignKey(Studio, on_delete=models.DO_NOTHING)
    genres = models.ManyToManyField(Genre)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

