from snippets.models import Snippet
from rest_framework import serializers

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    class Meta:
        model = Snippet
        fields = ('url','id','owner','title','code','highlight','linenos','language','style')