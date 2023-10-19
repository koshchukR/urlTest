from rest_framework.serializers import Serializer
from rest_framework import serializers


class ResultUrlSerializer(Serializer):
    message = serializers.CharField()
    risk_score = serializers.CharField()

    class Meta:
        fields = ('message', 'risk_score')


class SwaggerUrlSerializer(Serializer):
    domain_result = ResultUrlSerializer()
    content_result = ResultUrlSerializer()
    transmit_data_result = ResultUrlSerializer()
    overall_risk = serializers.CharField()

    class Meta:
        fields = ('domain_result', 'content_result', 'transmit_data_result', 'overall_risk')
