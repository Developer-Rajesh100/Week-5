from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=50)
    album_release_date = models.DateField("Date", auto_now_add=True)
    rating = models.IntegerField()
    musician = models.ForeignKey(Musician, related_name='albums', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.album_name} | {self.album_release_date} | {self.rating} | {self.musician.first_name} {self.musician.last_name}"