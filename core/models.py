from datetime import datetime
from django.db import models

"""
Модели:
    Teachers
    Lectures
    TimeTable
    Groups
    Students
"""


class Teacher(models.Model):
    name_full = models.CharField(max_length=255, verbose_name='Преподаватель')
    specialization = models.CharField(max_length=255, verbose_name='Специальность')

    def __str__(self):
        return self.name_full


class Group(models.Model):
    group_number = models.IntegerField(verbose_name='Номер группы')

    def __str__(self):
        return f'Группа №{str(self.group_number)}'


class Lecture(models.Model):
    lection_name = models.CharField(max_length=255, verbose_name='Название лекции')
    start_time = models.DateTimeField(null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, related_name='lectures')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.lection_name


class Student(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО студента')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, related_name='students')
    subscription = models.BooleanField(default=False)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.full_name
