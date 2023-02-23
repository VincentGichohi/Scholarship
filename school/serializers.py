from rest_framework import serializers
from .models import School, Course


class SchoolAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class CourseAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

