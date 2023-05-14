"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


description_str = (
    "This is a imdevEdu API. You can find out more about imdevEdu at https://m-d-n.github.io/imdevEdu/index.html."
    "Use the api key special-key to work with the authorization filters."
    "Swagger API - imdevEdu (Курсы IMDEV)"
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include("apps.account.url")),
    path("", include("apps.course.url")),
]

merchant_schema_view_standard = get_schema_view(
    openapi.Info(
        title="IMDEV API",
        default_version="v1",
        description=description_str,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="gicorp.work@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    patterns=urlpatterns,
    permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    re_path(
        r"^api/docs/$",
        merchant_schema_view_standard.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
