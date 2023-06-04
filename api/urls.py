from django.urls import path
from api.views import *

urlpatterns = [
    path('/records', RecordListCreateView.as_view(), name='record-list-create'),
    path('/auth/token/', TokenView.as_view(), name='token'),
]
