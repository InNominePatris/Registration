from django.contrib import admin
from .models import Student, Parent
from enrollments.admin import RegisterInline


class StudentInline(admin.TabularInline):
    model = Student


class ParentAdmin(admin.ModelAdmin):
    inlines = [StudentInline]


class StudentAdmin(admin.ModelAdmin):
    inlines = [RegisterInline]


admin.site.register(Student, StudentAdmin)
admin.site.register(Parent, ParentAdmin)

