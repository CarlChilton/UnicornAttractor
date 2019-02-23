from django.conf.urls import url
from dashboard.views import index
from bugs.views import bugs, create_or_edit_bug, bug_detail

urlpatterns = [
    url(r'^/$', bugs, name="bugs"),
    url(r'^(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^new/$', create_or_edit_bug, name='new_bug'),
    # url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post'),
]