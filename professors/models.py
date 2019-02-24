from django.db import models
from students.models import Student
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class Professor(models.Model):
    GENDER_FEMALE = 'f'
    GENDER_MALE = 'm'

    GENDER_CHOICES = (
        (GENDER_FEMALE, _('Female')),
        (GENDER_MALE, _('Male'))
    )

    first_name = models.CharField(max_length=50, verbose_name=_('First_Name'))
    last_name = models.CharField(max_length=50, verbose_name=_('Last_name'))
    age = models.IntegerField(verbose_name=_('Age'),
                              validators=[MinValueValidator(0), MaxValueValidator(100)]
                              )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name=_('Gender'))
    birth = models.DateField(verbose_name=_('Birth'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = _('Professors')
        verbose_name = _('Professor')



