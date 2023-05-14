from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.account import api

router = DefaultRouter()
router.register(r"profile", api.ProfileAPI, basename="Profile")
router.register(r"user", api.UserAPI, basename="User")

urlpatterns = [
    path("api/", include(router.urls)),
]
