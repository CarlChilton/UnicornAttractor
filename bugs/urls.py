from django.conf.urls import url, include
from dashboard.views import index
from bugs.views import bugs, create_or_edit_bug, upvote_bug, add_comment, mark_done_bug, mark_doing_bug

urlpatterns = [
    url(r'^/$', bugs, name="bugs"),
    url(r'^(?P<pk>\d+)/$', add_comment, name="add_comment"),
    url(r'^upvote_bug/(?P<pk>\d+)/$', upvote_bug, name='upvote_bug'),
    url(r'^mark_done_bug/(?P<pk>\d+)/$', mark_done_bug, name='mark_done_bug'),
    url(r'^mark_doing_bug/(?P<pk>\d+)/$', mark_done_bug, name='mark_doing_bug'),
    url(r'^new/$', create_or_edit_bug, name='new_bug'),
]