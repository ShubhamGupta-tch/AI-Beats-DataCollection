from django.db import models

# Create your models here.
class Vocal(models.Model):
    email = models.CharField(max_length=128)
    song_name = models.CharField(max_length=512)
    song_url = models.URLField(max_length=1024)
    vocal_url = models.URLField(max_length=1024, blank=True)
    vocal = models.FileField(upload_to='vocals/', blank=True)

    def __str__(self):
        return f'{self.song_name} -> {self.email}'
