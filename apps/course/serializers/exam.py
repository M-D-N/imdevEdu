from rest_framework import serializers
from apps.course.models import Examination, TrialRecord, Question, Answer
from django.contrib.auth.models import User


class AnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            "id",
            "question",
            "name",
            "ordering",
            "is_correct",
            "is_active",
            "created_at",
        )


class QuestionDetailSerializer(serializers.ModelSerializer):
    answers = AnswerDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = (
            "id",
            "examination",
            "name",
            "description",
            "ordering",
            "is_active",
            "created_at",
            "answers",
        )


class ExaminationDetailSerializer(serializers.ModelSerializer):
    questions = QuestionDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Examination
        fields = (
            "id",
            "name",
            "course",
            "min_score",
            "max_score",
            "description",
            "is_active",
            "created_at",
            "questions",
        )


class TrialRecordCreateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    examination = serializers.PrimaryKeyRelatedField(
        queryset=Examination.objects.all(), required=True
    )
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=True
    )
    user_score = serializers.IntegerField(required=True)
    is_active = serializers.BooleanField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = TrialRecord
        fields = (
            "id",
            "examination",
            "user",
            "user_score",
            "is_active",
            "created_at",
        )


class TrialRecordDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrialRecord
        fields = (
            "id",
            "examination",
            "user",
            "user_score",
            "is_active",
            "is_completed",
            "created_at",
        )
