from django.db import models


# Create your models here.
# add blog app into setting, url, views, html ( might have done it already)

# create your models here


class Blog(models.Model):
    title = models.CharField(max_length=250)
    pug_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()


def __str__(self):
    return self.title

# title
# pug_date DateTimeField
# body TextField
# image ImageField

# makemigrations
# migrate
# add to admin
# def __str__

# update views
# update allblog.html
