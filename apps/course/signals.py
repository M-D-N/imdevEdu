from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.course.models import Achievement, TrialRecord


@receiver(post_save, sender=TrialRecord)
def create_user_achievement(sender, instance=None, created=False, **kwargs):
    if created and instance.is_completed:
        _, _ = Achievement.objects.get_or_create(
            user=instance.user,
            certificate=instance.examination.course.certificate,
        )
