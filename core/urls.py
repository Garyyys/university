from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('student/<int:pk>/', views.StudentAPIView.as_view()),
    path('student/add/', views.AddStudentToDB.as_view()),
    path('group/<int:pk>/', views.GroupAPIView.as_view()),
    path('group/add/', views.AddGroupToDB.as_view()),
    path('lecture/add/', views.AddLecturesToDB.as_view()),
    path('lecture/<int:pk>/', views.LectureAPIView.as_view()),
    path('teacher/<int:pk>/', views.TeacherAPIView.as_view()),
    path('teacher/add/', views.AddTeachersToDB.as_view()),
    path('schedule/', views.ScheduleAPIView.as_view()),
]