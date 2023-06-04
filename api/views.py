from index.models import Record
from .serializer import RecordSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from knox.auth import TokenAuthentication
from .filters import RecordFilter

from knox.auth import TokenAuthentication
from knox.models import AuthToken

class RecordListCreateView(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    filterset_class = RecordFilter
    search_fields = ['title', 'url']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TokenView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = AuthToken.objects.create(user)
        return Response({'token': token}, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
