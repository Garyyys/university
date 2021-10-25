from rest_framework import serializers
from .models import Student, Group, Lecture, Teacher
from datetime import datetime


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'name_full', 'specialization')
        read_only_fields = ('id',)


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'lection_name', 'start_time', 'group', 'teacher')
        read_only_fields = ('id',)


class GroupLectureSerializer(serializers.ModelSerializer):
    lectures = serializers.SerializerMethodField()

    def get_lectures(self, obj):
        date = datetime.strptime(
            self.context.get('request').query_params.get('date', datetime.now().strftime('%Y-%m-%d')),
            '%Y-%m-%d'
        ).date()
        student_pk = self.context.get('request').parser_context.get('kwargs').get('pk')
        lecture_qs = Lecture.objects.filter(group__students__pk=student_pk).filter(start_time__date=date)
        return LectureSerializer(many=True).to_representation(lecture_qs)

    class Meta:
        model = Group
        fields = ('id', 'group_number', 'lectures')
        read_only_fields = ('id',)


class StudentSerializer(serializers.ModelSerializer):
    group = GroupLectureSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'full_name', 'group', 'subscription', 'email')
        read_only_fields = ('id',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'group_number',)
        read_only_fields = ('id',)
