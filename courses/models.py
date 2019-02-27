from django.db import models
from django.utils.translation import ugettext_lazy as _
from grades.models import Assignature
from professors.models import Professor
from enrollments.models import Registration
from students.models import Student
from grades.models import Grade


class Course(models.Model):

    TYPE_MORNING = 'Mañana'
    TYPE_EVENING = 'Tarde'
    TYPE_NIGHT = 'Noche'

    TYPE_CHOICES = (
        (TYPE_MORNING, _('Morning')),
        (TYPE_EVENING, _('Evening')),
        (TYPE_NIGHT, _('Night')),
    )

    type = models.CharField(max_length=6, choices=TYPE_CHOICES, verbose_name=_('Type'))
    grade = models.ManyToManyField(Grade, verbose_name=_('Grade'))
    professor = models.ManyToManyField(Professor, verbose_name=_('Professor'))
    registration = models.ManyToManyField(Registration, verbose_name=_('Registration'))

    def __str__(self):
        return '{}'.format(self.type)

    class Meta:
        verbose_name_plural = _('Courses')
        verbose_name = _('Course')
