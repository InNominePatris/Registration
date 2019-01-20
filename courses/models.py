from django.db import models
from django.utils.translation import ugettext_lazy as _
from grades.models import Assignature
from professors.models import Professor
from enrollments.models import Registration
from students.models import Student
from grades.models import Grade


class Course(models.Model):

    TYPE_MORNING = 'm'
    TYPE_EVENING = 'e'
    TYPE_NIGHT = 'n'

    TYPE_CHOICES = (
        (TYPE_MORNING, _('Morning')),
        (TYPE_EVENING, _('Evening')),
        (TYPE_NIGHT, _('Night')),
    )

    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    grade = models.ManyToManyField(Grade)
    professor = models.ManyToManyField(Professor)
    registration = models.ManyToManyField(Registration)


