from rest_framework import serializers
from apps.course.models import Course, Module, Enrollment
from django.contrib.auth.models import User


class ModuleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = (
            "id",
            "course",
            "name",
            "description",
            "image",
            "ordering",
            "is_active",
            "created_at",
        )


class CourseDetailSerializer(serializers.ModelSerializer):
    modules = ModuleDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "description",
            "image",
            "ordering",
            "is_active",
            "created_at",
            "examination_id",
            "modules",
        )


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "description",
            "image",
            "ordering",
            "is_active",
            "created_at",
        )


class EnrollmentCreateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    course = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), required=True
    )
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=True
    )
    is_active = serializers.BooleanField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Enrollment
        fields = (
            "id",
            "course",
            "user",
            "is_active",
            "created_at",
        )
