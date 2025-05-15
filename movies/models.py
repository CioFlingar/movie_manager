from django.db import models

# Create your models here.

class MovieData(models.Model):

    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    typ =  models.CharField(max_length=200, default='action')
    image = models.ImageField(upload_to="Images/", default="Images/candles.webp", blank=True)
