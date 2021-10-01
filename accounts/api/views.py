from rest_framework.response import Response
from .serializers import LoginSerializer, RegisterSerializer, EmptySerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework import viewsets
from django.core.exceptions import ImproperlyConfigured
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

# another type of class to use


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [
        AllowAny,
    ]
    serializer_classe = EmptySerializer
    serializer_classes = {
        "login": LoginSerializer,
        "register": RegisterSerializer,
    }

    @action(
        methods=[
            "POST",
        ],
        detail=False,
    )
    def login(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data.get("user")
        if user is not None and user.is_active:
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(
        methods=[
            "POST",
        ],
        detail=False,
    )
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password1"]
            user = User.objects.create_user(
                username=username, password=password
            )
            authenticate(request, username=username, password=password)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(
        methods=[
            "GET",
        ],
        detail=False,
    )
    def logout(self, request):
        logout(request)
        data = {"success": "Sucessfully logged out"}
        return Response(data=data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured(
                "serializer_classes should be a dict mapping."
            )

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()


class LogoutViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        logout(request)
        return Response(
            {"non_field_errors": "successfully logged out"},
            status=status.HTTP_200_OK,
        )


class RegisterViewSet(viewsets.ViewSet):
    serializer_class = RegisterSerializer

    def create(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        serializer = RegisterSerializer(data=request.data, many=False)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password1"]
            user = User.objects.create_user(
                username=username, password=password
            )
            authenticate(request, username=username, password=password)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        """
        Login view to get user credentials
        """
        serializer = LoginSerializer(data=request.data, many=False)

        if serializer.is_valid():
            user = serializer.validated_data.get("user")
            if user is not None and user.is_active:
                login(request, user)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
