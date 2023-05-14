from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, pagination, permissions, viewsets
from rest_framework.authentication import TokenAuthentication

from apps.course.models import Course, Enrollment
from apps.course.serializers import (
    CourseListSerializer,
    CourseDetailSerializer,
    EnrollmentCreateSerializer,
)


@swagger_auto_schema(request_body=Course, tags=["Course"])
class CourseAPI(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    action_serializers = {
        "list": CourseListSerializer,
        "retrieve": CourseDetailSerializer,
    }
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.PageNumberPagination

    page_size = 10

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(CourseAPI, self).get_serializer_class()

    @swagger_auto_schema(
        operation_description="List courses",
        operation_summary="List courses",
        responses={200: CourseListSerializer},
        tags=["Course"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Read a course by id",
        operation_summary="Read a course by id",
        responses={200: CourseDetailSerializer},
        tags=["Course"],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


@swagger_auto_schema(request_body=Enrollment, tags=["Enrollment"])
class EnrollmentAPI(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Enrollment.objects.all()
    action_serializers = {
        "create": EnrollmentCreateSerializer,
        "destroy": None,
    }
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(EnrollmentAPI, self).get_serializer_class()

    @swagger_auto_schema(
        operation_description="Add a user to the given course by id",
        operation_summary="Add a user to the given course by id",
        responses={200: EnrollmentCreateSerializer},
        tags=["Enrollment"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Remove a user from the given course by id",
        operation_summary="Remove a user from the given course by id",
        tags=["Enrollment"],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
