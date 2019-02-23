from django.conf.urls import url
from dashboard.views import index
from bugs.views import bugs

urlpatterns = [
    url(r'^/$', bugs, name="bugs"),
]