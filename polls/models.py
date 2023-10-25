from django.db import models


class Topics(models.Model):
    topic = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.topic}"


class Books(models.Model):
    name = models.CharField(max_length=30)
    topic = models.PositiveSmallIntegerField()
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Votes(models.Model):
    topic = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    book_id = models.PositiveIntegerField()
