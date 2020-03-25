from django.db import models


class Blog(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

    def summary(self):
        list_words = self.body.split()
        text = " ".join(list_words[:10]) + '...'
        return text

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
# Create your models here.
