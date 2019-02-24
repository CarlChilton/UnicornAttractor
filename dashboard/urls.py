from django.conf.urls import url
from dashboard.views import index, bugsByMonth, featuresByMonth

urlpatterns = [
    url(r'^/$', index, name="index"),
    url(r'^bugsByMonth/$', bugsByMonth, name='bugsByMonth'),
    url(r'^featuresByMonth/$', featuresByMonth, name='featuresByMonth'),
]



