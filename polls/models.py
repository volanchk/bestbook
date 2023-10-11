from django.db import models


class Topic(models.Model):
    topic = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
