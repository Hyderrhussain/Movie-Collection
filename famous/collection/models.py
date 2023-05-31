from django.db import models

class movie(models.Model):
    movieid = models.CharField(max_length=100)
    moviename = models.CharField(max_length=100)
    moviedirector= models.CharField(max_length=100)
    releasedate = models.DateField(null=True)

    class Meta:
        db_table = "movie"
