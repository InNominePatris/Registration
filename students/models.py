from django.db import models
from django.utils.translation import ugettext_lazy as _


class Parent(models.Model):
    GENDER_FEMALE = 'f'
    GENDER_MALE = 'm'

    GENDER_CHOICES = (
        (GENDER_FEMALE, _('Female')),
        (GENDER_MALE, _('Male'))
    )

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Student(models.Model):
    GENDER_FEMALE = 'f'
    GENDER_MALE = 'm'

    GENDER_CHOICES = (
        (GENDER_FEMALE, _('Female')),
        (GENDER_MALE, _('Male'))
    )

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    parent = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE
    )
    birthday = models.DateField()
    Address = models.CharField(max_length=150)
    Phone = models.CharField(max_length=8)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


