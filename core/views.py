from django.shortcuts import render
from .serializers import StudentSerializer, GroupLectureSerializer, GroupSerializer, LectureSerializer, \
    TeacherSerializer
from .models import Student, Group, Lecture, Teacher

from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from datetime import datetime

class StudentAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all().select_related('group').prefetch_related('group__lectures')


class AddStudentToDB(CreateAPIView):
    serializer_class = StudentSerializer


class GroupAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class AddGroupToDB(CreateAPIView):
    serializer_class = GroupSerializer


class LectureAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()


class AddLecturesToDB(CreateAPIView):
    serializer_class = LectureSerializer


class TeacherAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class AddTeachersToDB(CreateAPIView):
    serializer_class = TeacherSerializer


class ScheduleAPIView(ListAPIView):
    serializer_class = LectureSerializer
    queryset = Lecture.objects.filter(start_time__date=datetime.now().date())

