from index.models import Record
from .serializer import RecordSerializer, TokenSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from knox.auth import TokenAuthentication
from .filters import RecordFilter

from knox.auth import TokenAuthentication
from knox.models import AuthToken

class RecordListCreateView(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = RecordFilter
    search_fields = ['title', 'url']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TokenView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    serializer_class = TokenSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = AuthToken.objects.create(user)
        return Response({
            'token': token[1],
        })

    def delete(self, request, *args, **kwargs):
        user_token = request.auth
        if user_token:
            request.user.auth_token.delete()
            user_token.delete()
            return Response({'detail': 'Token invalidated'})
        else:
            return Response({'detail': 'No token provided'})
