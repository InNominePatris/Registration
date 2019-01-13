from django.contrib import admin
from .models import Assignature, Grade


class AssignatureInline(admin.TabularInline):
    model = Assignature

    admin.site.register(Assignature)
    admin.site.register(Grade)

