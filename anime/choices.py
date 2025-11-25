from django.db import models

class AnimeStatus(models.TextChoices):
    ANNOUNCED = 'announced', 'Announced'
    HIATUS = 'hiatus', 'Hiatus'
    FINISHED = 'finished', 'Finished'
