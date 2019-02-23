from django.conf.urls import url, include
from dashboard.views import index
from bugs.views import bugs, create_or_edit_bug, bug_detail, upvote_bug, add_comment

urlpatterns = [
    url(r'^/$', bugs, name="bugs"),
    url(r'^(?P<pk>\d+)/$', add_comment, name="add_comment"),
    url(r'^(?P<pk>\d+)/$', upvote_bug, name='upvote_bug'),
    url(r'^(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^new/$', create_or_edit_bug, name='new_bug'),
]