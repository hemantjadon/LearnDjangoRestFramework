from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view(),name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(),name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(),name = 'snippet-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)