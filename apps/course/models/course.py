import uuid

from django.db import models
from django.utils import timezone


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, upload_to="media/courses")
    url = models.CharField(max_length=250, blank=True, null=True)
    ordering = models.PositiveIntegerField(default=0, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        editable=False,
        default=timezone.now,
        null=True,
    )

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    @property
    def examination_id(self):
        return str(self.examination.id)


class Module(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(
        "course.Course",
        on_delete=models.CASCADE,
        null=True,
        related_name="modules",
    )
    name = models.CharField(max_length=250, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to="media/modules")
    ordering = models.PositiveIntegerField(default=0, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        editable=False,
        default=timezone.now,
        null=True,
    )

    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Modules"


class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(
        "course.Course",
        on_delete=models.CASCADE,
        null=True,
        related_name="users",
    )
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        null=True,
        related_name="courses",
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        editable=False,
        default=timezone.now,
        null=True,
    )

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"
