from snippets.models import Snippets
from snippets.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippet, or create a new snippet.
    """
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
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
