from django.conf.urls import url
from accounts.views import accounts

urlpatterns = [
    url(r'^/$', accounts, name="accounts"),
]
