from django.contrib import admin
from .models import Registration


class RegisterInline(admin.TabularInline):
    model = Registration


admin.site.register(Registration)
