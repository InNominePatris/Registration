from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class Parent(models.Model):
    GENDER_FEMALE = 'f'
    GENDER_MALE = 'm'

    GENDER_CHOICES = (
        (GENDER_FEMALE, _('Female')),
        (GENDER_MALE, _('Male'))
    )

    first_name = models.CharField(max_length=50,verbose_name=_('First name'))
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = _('Parents')
        verbose_name = _('Parent')


class Student(models.Model):
    GENDER_FEMALE = 'f'
    GENDER_MALE = 'm'

    GENDER_CHOICES = (
        (GENDER_FEMALE, _('Female')),
        (GENDER_MALE, _('Male'))
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    parent = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE
    )
    birthday = models.DateField()
    address = models.CharField(max_length=50)
    phone = PhoneNumberField()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)