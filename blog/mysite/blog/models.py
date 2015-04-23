from django.db import models

# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
