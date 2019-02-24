from django.conf.urls import url, include
from dashboard.views import index
from features.views import features, create_or_edit_feature, upvote_feature, add_comment

urlpatterns = [
    url(r'^/$', features, name="features"),
    url(r'^(?P<pk>\d+)/$', add_comment, name="add_comment"),
    url(r'^upvote_feature/(?P<pk>\d+)/$', upvote_feature, name='upvote_feature'),
    url(r'^new/$', create_or_edit_feature, name='new_feature'),
]