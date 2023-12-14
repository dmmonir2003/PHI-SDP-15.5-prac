from django import forms
from . import models

class AlbumForm(forms.ModelForm):
    class Meta:
        model = models.AlbumModel
        exclude = ('album_release_date',)
