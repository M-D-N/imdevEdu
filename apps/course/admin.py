from django.contrib import admin
from .models import (
    Course,
    Module,
    Enrollment,
    Certificate,
    TrialRecord,
    Examination,
    Achievement,
    Question,
    Answer,
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    pass


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass


@admin.register(TrialRecord)
class TrialRecordAdmin(admin.ModelAdmin):
    pass


@admin.register(Examination)
class ExaminationAdmin(admin.ModelAdmin):
    pass


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
