from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from core.calculate_weighted_risk_score import calculate_weighted_risk_score
from core.content_is_loaded_externally import content_is_loaded_externally
from core.how_old_is_domain import how_old_is_domain
from core.webform_to_transmit_data import webform_to_transmit_data

from .serializers import UrlSerializer

from drf_yasg.utils import swagger_auto_schema

from .swagger.serializers import SwaggerUrlSerializer


class CheckUrlView(GenericAPIView):
    """
    Check url
    """

    permission_classes = (IsAuthenticated,)
    throttle_classes = (AnonRateThrottle, UserRateThrottle)
    serializer_class = UrlSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: SwaggerUrlSerializer()})
    def post(self, *args, **kwargs):
        data = self.request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        try:
            domain_result = how_old_is_domain(data['url'])
            content_externally_result = content_is_loaded_externally(data['url'])
            transmit_data_from_webform = webform_to_transmit_data(data['url'])

        except Exception as e:
            return Response({"message": f"Could not determine the results for {data['url']}."},
                            status.HTTP_400_BAD_REQUEST)

        check1_score = domain_result['risk_score']  # Example score from check 1
        check2_score = content_externally_result['risk_score']  # Example score from check 2
        check3_score = transmit_data_from_webform['risk_score']  # Example score from check 3

        # Calculate the overall risk score
        overall_risk = calculate_weighted_risk_score(
            [check1_score, check2_score, check3_score]
        )

        return Response({"domain_result": domain_result, "content_result": content_externally_result,
                         "transmit_data_result": transmit_data_from_webform, "overall_risk": f"{overall_risk:.2f}"},
                        status=status.HTTP_200_OK)
