from django.db import models

# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length=30)
    vector = models.FloatField()

    def __str__(self):
        return self.word
