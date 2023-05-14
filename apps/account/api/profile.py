from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, permissions, viewsets
from rest_framework.authentication import TokenAuthentication

from apps.account.models import Profile
from apps.account.serializer import ProfileDetailSerializer


@swagger_auto_schema(request_body=Profile, tags=["Profile"])
class ProfileAPI(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    action_serializers = {
        "retrieve": ProfileDetailSerializer,
    }
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(ProfileAPI, self).get_serializer_class()

    @swagger_auto_schema(
        operation_description="Read a course by id",
        operation_summary="Read a course by id",
        responses={200: ProfileDetailSerializer},
        tags=["Profile"],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
