from django.urls import path
from paytm.views import get_details, response

urlpatterns = [
    path('', get_details, name='detail'),
    path('response/', response, name='response'),
]