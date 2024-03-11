from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    user = request.user
    Token.objects.get(user=user).delete()
    response = {
        "success": True,
        "message": "Successfully logged out"
    }
    return Response(response, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method="POST",
    reuqest_body=openapi.Schema(
        type="object",
        properties={
            "username": openapi.Schema(type=openapi.TYPE_STRING),
            "password1": openapi.Schema(type=openapi.TYPE_STRING),
            "password2": openapi.Schema(type=openapi.TYPE_STRING),
        },
        required=["username", "password1", "password2"],
        example={
            "username": "",
            "password1": "",
            "password2": ""
        }
    ),
    responses={
        200: openapi.Response(description="Success response"),
        400: openapi.Response(description="Bad request"),
    }
)
@api_view(["POST"])
def register_view(request):
    data = request.data
    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

