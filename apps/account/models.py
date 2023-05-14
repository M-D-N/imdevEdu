import uuid

from django.db import models
from django.utils import timezone


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        "auth.User",
        null=True,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    image = models.FileField(null=True, blank=True, upload_to="media/profiles")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        editable=False,
        default=timezone.now,
        null=True,
    )

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    @property
    def courses(self):
        return self.user.courses.order_by("-created_at")

    @property
    def certificates(self):
        return self.user.certificates.order_by("-created_at")

    @property
    def exam_trials(self):
        return self.user.trials.order_by("-created_at")
