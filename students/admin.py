from django.contrib import admin
from .models import Student, Parent
from enrollments.admin import RegisterInline
from django.contrib.auth.models import User, Group
from django.contrib.admin.models import LogEntry


class StudentInline(admin.TabularInline):
    model = Student


list_display = ('first_name', 'last_name', 'parent')


class ParentAdmin(admin.ModelAdmin):
    inlines = [StudentInline]


class StudentAdmin(admin.ModelAdmin):
    inlines = [RegisterInline]


admin.site.register(Student, StudentAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)