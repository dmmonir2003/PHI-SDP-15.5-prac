from django.db import models
from musician.models import MusicianModel
# Create your models here.
RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )


class AlbumModel(models.Model):
    album_name=models.CharField(max_length=100)
    album_release_date=models.DateField(auto_now=True)
    rating = models.IntegerField(choices=RATING_CHOICES)
    musician=models.ForeignKey(MusicianModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name
    

