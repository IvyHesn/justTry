from django.db import models

# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    tag = models.CharField(max_length=20)
    pub_date = models.DateTimeField(
        'pub_date', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('update_time', auto_now=True, null=True)

    def __str__(self):  # use __unicode__(self) on Python2
        return self.name
