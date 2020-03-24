from django.db import models


class Blog(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images')


# Create your models here.
