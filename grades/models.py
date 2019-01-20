from django.db import models


class Assignature(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)


class Grade(models.Model):
    name = models.CharField(max_length=50)
    Assignature = models.ManyToManyField(Assignature)

    def __str__(self):
        return '{}'.format(self.name)