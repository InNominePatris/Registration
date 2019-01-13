from django.db import models


class Assignature(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


    def __str__(self):
        return '{} {}'.format(self.name, self.description)


class Grade(models.Model):
    name = models.CharField(max_length=150)
    Assignature = models.ManyToManyField(Assignature)

    def __str__(self):
        return '{}'.format(self.name)