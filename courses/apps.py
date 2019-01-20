from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CourseConfig(AppConfig):
    name = 'courses'


verbose_name = _('Courses')