import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class Book(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200, blank=True)
    info = models.CharField(max_length=200, blank=True)
    summary = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.title + " -- " + self.author



