from rest_framework import serializers
from account.models import Member
from resource.serializers import FileSerializer
from deadline.serializers import DeadlineSerializer
from .models import *


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["id", "code", "name", "email", "image"]


class CourseSerializer(serializers.ModelSerializer):
    course_lecturer = LectureSerializer(many=True, read_only=True)
    created_by = LectureSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ["id", "mskh", "name", "description", "created_by", "course_lecturer"]


class LessonSerializer(serializers.ModelSerializer):
    file_lesson = FileSerializer(many=True, read_only=True)
    deadline_lesson = DeadlineSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = "__all__"
        read_only_fields = ["course"]


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
