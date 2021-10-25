from django.contrib import admin
from .models import Teacher, Lecture, Group, Student


# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """ тут отображаем филды в админке"""
    list_display = ('name_full', 'specialization')


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('lection_name',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_number',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'group')
