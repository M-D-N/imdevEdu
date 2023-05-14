from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response


from apps.account.serializer import UserDetailSerializer, LoginSerializer


@swagger_auto_schema(request_body=UserDetailSerializer, tags=["User"])
class UserAPI(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    action_serializers = {
        "login": LoginSerializer,
        "logout": None,
    }
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(UserAPI, self).get_serializer_class()

    @swagger_auto_schema(
        operation_description="Login by username and password",
        operation_summary="User login",
        tags=["User"],
    )
    @action(
        detail=False,
        url_path="login",
        name="login",
        methods=["post"],
        authentication_classes=[],
        permission_classes=[permissions.AllowAny],
    )
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(
                serializer.validated_data.get("username"),
                serializer.validated_data.get("password"),
            )
            user = authenticate(
                username=serializer.validated_data.get("username"),
                password=serializer.validated_data.get("password"),
            )
            print(user)
            if user is None:
                return Response(
                    {"error": "Invalid username/password. Please try again!"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            token, _ = Token.objects.get_or_create(user=user)
            user_serialized = UserDetailSerializer(user)
            auth.login(request, user)
            return Response(
                {
                    "user": user_serialized.data,
                    "token": token.key,
                    "profile": user.profile.id,
                },
                status=status.HTTP_200_OK,
            )

    @swagger_auto_schema(
        operation_description="Logout current user",
        operation_summary="User logout",
        tags=["User"],
    )
    @action(
        detail=False,
        url_path="logout",
        name="logout",
        methods=["POST"],
        permission_classes=[permissions.IsAuthenticated],
        serializer_class=None,
    )
    def logout(self, request):
        auth.logout(request)
        return Response({"You are logged out!"}, status=status.HTTP_200_OK)
