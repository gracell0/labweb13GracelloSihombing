# basic_api/models.py
from django.db import models

#list
Grade = [
    ('excellent', 1),
    ('average', 0),
    ('bad', -1)
]

# DataFlair
class DRFPost(models.Model):
    name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    uploaded = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = Grade, default = 'average', max_length = 50)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

    class Meta:
        ordering = ['uploaded']

    def __str__(self):
        return self.name

from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    rating = models.CharField(max_length=20)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)  # Field untuk gambar
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name