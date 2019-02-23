from django.conf.urls import url
from features.views import features

urlpatterns = [
    url(r'^/$', features, name="features"),
]
