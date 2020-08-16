from django.db import models

# Create your models here.


class BookModel(models.Model):
    book_id = models.CharField(max_length=3)
    name = models.CharField(max_length=75)
    writer = models.CharField(max_length=50)
