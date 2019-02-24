from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class GradesConfig(AppConfig):
    name = 'grades'

    verbose_name = _('Grades')
