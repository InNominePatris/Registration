from django.db import models
from students.models import Student
from django.utils.translation import ugettext_lazy as _


class Registration(models.Model):
    date = models.DateField(verbose_name=_('Date'))
    is_active = models.BooleanField(default=False, verbose_name=_('Is_active'))
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_('Student'))

    def __str__(self):
        return '{} {}'.format(self.date, self.student)

    class Meta:
        verbose_name_plural =_('Enrollments')
        verbose_name = _('Enrollment')
