from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, pagination, permissions, viewsets
from rest_framework.authentication import TokenAuthentication

from apps.course.models import Examination, TrialRecord
from apps.course.serializers import (
    ExaminationDetailSerializer,
    TrialRecordCreateSerializer,
)


@swagger_auto_schema(request_body=Examination, tags=["Examination"])
class ExaminationAPI(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Examination.objects.all()
    serializer_class = ExaminationDetailSerializer
    action_serializers = {
        "retrieve": ExaminationDetailSerializer,
    }
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.PageNumberPagination

    page_size = 10

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(ExaminationAPI, self).get_serializer_class()

    @swagger_auto_schema(
        operation_description="Read an examination by id",
        operation_summary="Read an examination by id",
        responses={200: ExaminationDetailSerializer},
        tags=["Examination"],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


@swagger_auto_schema(request_body=TrialRecord, tags=["Trial Record"])
class TrialRecordAPI(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = TrialRecord.objects.all()
    action_serializers = {
        "create": TrialRecordCreateSerializer,
    }
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(TrialRecordAPI, self).get_serializer_class()

    @swagger_auto_schema(
        operation_description="Add a user try to the given exam by id",
        operation_summary="Add a user try to the given exam by id",
        responses={200: TrialRecordCreateSerializer},
        tags=["Trial Record"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
