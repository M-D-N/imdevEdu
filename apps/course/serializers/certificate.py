from rest_framework import serializers
from apps.course.models import Achievement, Certificate


class CertificateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
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


class AchievementDetailSerializer(serializers.ModelSerializer):
    certificate = CertificateDetailSerializer(read_only=True)

    class Meta:
        model = Achievement
        fields = (
            "id",
            "user",
            "certificate",
            "is_verified",
            "created_at",
        )
