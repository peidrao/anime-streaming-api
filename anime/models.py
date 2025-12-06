from django.db import models


class Studio(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Studio"
        verbose_name_plural = "Studios"
        db_table = 'studios'


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        db_table = 'genres'


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        db_table = 'tags'

