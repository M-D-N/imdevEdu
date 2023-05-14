from rest_framework import serializers

from apps.account.models import Profile
from django.contrib.auth.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        fields = ("username", "password")


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class ProfileDetailSerializer(serializers.ModelSerializer):
    from apps.course.serializers import (
        CourseListSerializer,
        AchievementDetailSerializer,
        TrialRecordDetailSerializer,
    )

    user = UserDetailSerializer(read_only=True)
    courses = CourseListSerializer(read_only=True, many=True)
    certificates = AchievementDetailSerializer(read_only=True, many=True)
    exam_trials = TrialRecordDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "image",
            "is_active",
            "created_at",
            "courses",
            "certificates",
            "exam_trials",
        )
