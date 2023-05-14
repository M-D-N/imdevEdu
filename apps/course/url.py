from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.course import api

router = DefaultRouter()
router.register(r"course", api.CourseAPI, basename="Course")
router.register(r"enrollment", api.EnrollmentAPI, basename="Enrollment")
router.register(r"exam", api.ExaminationAPI, basename="Examination")
router.register(r"exam-trials", api.TrialRecordAPI, basename="Exam Trials")


urlpatterns = [
    path("api/", include(router.urls)),
]
