from django.db import models
from students.models import Student


class Registration(models.Model):
    date = models.DateField()
    is_active = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.date, self.student)
