from django.conf.urls import url, include
from dashboard.views import index
from features.views import features, create_or_edit_feature, upvote_feature, add_comment, payment, mark_doing_feature, mark_done_feature

urlpatterns = [
    url(r'^/$', features, name="features"),
    url(r'^(?P<pk>\d+)/$', add_comment, name="add_comment"),
    url(r'^upvote_feature/(?P<pk>\d+)/$', upvote_feature, name='upvote_feature'),
    url(r'^mark_doing_feature/(?P<pk>\d+)/$', mark_doing_feature, name='mark_doing_feature'),
    url(r'^mark_done_feature/(?P<pk>\d+)/$', mark_done_feature, name='mark_done_feature'),
    url(r'^new/$', create_or_edit_feature, name='new_feature'),
    url(r'^payment/(?P<pk>\d+)/$', payment, name='payment'),
]