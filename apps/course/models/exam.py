import uuid

from django.db import models
from django.utils import timezone


class Examination(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.OneToOneField(
        "course.Course",
        on_delete=models.CASCADE,
        null=True,
        related_name="examination",
    )
    name = models.CharField(max_length=250, null=True)
    min_score = models.IntegerField(default=0, null=True)
    max_score = models.IntegerField(default=10, null=True)
    description = models.TextField(null=True, blank=True)
    ordering = models.PositiveIntegerField(default=0, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        editable=False,
        default=timezone.now,
        null=True,
    )

    class Meta:
        verbose_name = "Examination"
        verbose_name_plural = "Examination"


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    examination = models.ForeignKey(
        "course.Examination",
        on_delete=models.CASCADE,
        null=True,
        related_name="questions",
    )
    name = models.CharField(max_length=1200, null=True)
    description = models.TextField(null=True, blank=True)
    ordering = models.PositiveIntegerField(default=0, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        editable=False,
        default=timezone.now,
        null=True,
    )

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(
        "course.Question",
        on_delete=models.CASCADE,
        null=True,
        related_name="answers",
    )
    name = models.CharField(max_length=1200, null=True)
    ordering = models.PositiveIntegerField(default=0, null=True)
    is_correct = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        editable=False,
        default=timezone.now,
        null=True,
    )

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"


class TrialRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    examination = models.ForeignKey(
        "course.Examination",
        on_delete=models.CASCADE,
        null=True,
        related_name="trials",
    )
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        null=True,
        related_name="trials",
    )
    user_score = models.IntegerField(default=0, null=True)
    ordering = models.PositiveIntegerField(default=0, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        editable=False,
        default=timezone.now,
        null=True,
    )

    class Meta:
        verbose_name = "Trial Record"
        verbose_name_plural = "Trial Record"

    @property
    def is_completed(self):
        return (
            self.examination.min_score <= self.user_score <= self.examination.max_score
        )
