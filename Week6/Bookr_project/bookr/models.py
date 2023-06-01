from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publication_date = models.DateField()
    rating = models.FloatField()
    num_reviews = models.IntegerField()


    