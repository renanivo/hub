from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^tags/(?P<tag_id>\d+)/$', views.TagsListView.as_view(), name='tags_list'),
    url(r'^get_tags_json/$', views.get_tags_json, name='get_tags_json'),
]
