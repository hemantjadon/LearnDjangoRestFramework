from snippets.models import Snippet
from rest_framework import serializers

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('id','owner','title','code','linenos','language','style')