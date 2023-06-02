from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('linkUpload', RecordCreateView.as_view(), name='record-create'),
]
