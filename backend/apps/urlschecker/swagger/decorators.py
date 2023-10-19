from django.utils.decorators import method_decorator

from rest_framework import status

from .serializers import SwaggerUrlSerializer

from drf_yasg.utils import swagger_auto_schema


def url_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_200_OK: SwaggerUrlSerializer(),
        }, security=[]),
        'post'
    )
