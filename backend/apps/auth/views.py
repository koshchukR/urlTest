from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status

from apps.auth.swagger.serializers import SwaggerUserSerializer
from apps.users.serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema


class AuthRegisterView(GenericAPIView):
    """
    Register user
    """

    serializer_class = UserSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: SwaggerUserSerializer()}, security=[])
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
