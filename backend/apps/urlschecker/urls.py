from django.urls import path

from .views import CheckUrlView

urlpatterns = [
    path('', CheckUrlView.as_view(), name='check_url')
]