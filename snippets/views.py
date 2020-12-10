from snippets.models import Snippets
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippet, or create a new snippet.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
    """
    List all user, or create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve a new user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
