"""
User and Snippets model serializer.
"""
from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippets


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
    Snippet Model Serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippets-highlight', format='html')

    class Meta:
        model = Snippets
        fields = ['url', 'id', 'highlight', 'title',
                  'code', 'linenos', 'language', 'style', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    User Model Serializer.
    """
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippets-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
