from django.db import models
from django.utils.translation import ugettext_lazy as _


class Assignature(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Name'),unique=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = _('Assignatures')
        verbose_name = _('Assignature')


class Grade(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Name'), unique=True)
    Assignature = models.ManyToManyField(Assignature, verbose_name=_('Assignature'))

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = _('Grades')
        verbose_name = _('Grade')