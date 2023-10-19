from django.utils.decorators import method_decorator

from rest_framework import status

from .serializers import SwaggerUserSerializer

from drf_yasg.utils import swagger_auto_schema


def token_pair_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_200_OK: SwaggerUserSerializer(),
        }, security=[]),
        'post'
    )
