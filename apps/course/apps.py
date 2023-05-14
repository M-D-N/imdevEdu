from django.apps import AppConfig


class CourseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.course"

    def ready(self):
        from apps.course import signals
