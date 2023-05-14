import uuid

from django.db import models
from django.utils import timezone


class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.OneToOneField(
        "course.Course",
        on_delete=models.CASCADE,
        null=True,
        related_name="certificate",
    )
    name = models.CharField(max_length=250, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, upload_to="media/certificates")
    ordering = models.PositiveIntegerField(default=0, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        editable=False,
        default=timezone.now,
        null=True,
    )

    class Meta:
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"


class Achievement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        null=True,
        related_name="certificates",
    )
    certificate = models.ForeignKey(
        "course.Certificate",
        on_delete=models.CASCADE,
        null=True,
        related_name="templates",
    )
    is_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        editable=False,
        default=timezone.now,
        null=True,
    )

    class Meta:
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"
