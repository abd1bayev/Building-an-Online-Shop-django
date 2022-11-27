from django.db import models

class Post(models.Model):
    lactation = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    adult = models.IntegerField()
    children = models.IntegerField()
    room = models.IntegerField()

    def __str__(self):
        return self.lactation