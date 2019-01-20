from django.db import models
from students.models import Student
from django.utils.translation import ugettext_lazy as _


class Professor(models.Model):
    GENDER_FEMALE = 'f'
    GENDER_MALE = 'm'

    GENDER_CHOICES = (
        (GENDER_FEMALE, _('Female')),
        (GENDER_MALE, _('Male'))
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth = models.DateField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=8)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)



