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

    first_name = models.CharField(max_length=50, verbose_name=_('First name'))
    last_name = models.CharField(max_length=50, verbose_name=_('Second_name'))
    age = models.IntegerField(
        verbose_name=_('Age'),
        validators=[MinValueValidator(35), MaxValueValidator(100)]
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name=_('Gender'))

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

    first_name = models.CharField(max_length=50, verbose_name=_('First_name'))
    last_name = models.CharField(max_length=50, verbose_name=_('Second_name'))
    age = models.IntegerField(
        verbose_name=_('Age'),
        validators=[MinValueValidator(18), MaxValueValidator(50)]
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name=_('Gender'))
    parent = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE, verbose_name=_('Padre')
    )
    birthday = models.DateField(verbose_name=_('Birthday'))
    address = models.CharField(max_length=50, verbose_name=_('Address'))
    phone = PhoneNumberField(verbose_name=_('Phone'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = _('Students')
        verbose_name = _('Student')
