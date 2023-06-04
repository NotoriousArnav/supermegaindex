from django.urls import path, include
from api.views import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

class APIRoot(APIView):
    """
    Custom API root view to display all available endpoints.
    """
    def get(self, request, format=None):
        data = {
            'Records Rest Endpoint': reverse('record-list-create', request=request, format=format),
            'API Auth Token Endpoint': reverse('token', request=request, format=format),
            # Add more endpoint URLs here
        }
        return Response(data)

urlpatterns = [
    path('/records', RecordListCreateView.as_view(), name='record-list-create'),
    path('/auth/token/', TokenView.as_view(), name='token'),
    path('/', APIRoot.as_view(), name='Endpoints')
]

