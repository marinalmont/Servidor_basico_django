from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    debut_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, related_name='songs', on_delete=models.CASCADE)
    duration = models.DurationField()

    def __str__(self):
        return self.title


