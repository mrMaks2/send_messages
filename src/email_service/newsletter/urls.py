from django.conf.urls import url
from .views import create_newsletter, track_open

urlpatterns = [
    url(r'^create/$', create_newsletter, name='create_newsletter'),
    url(r'^track_open/(?P<campaign_id>\d+)/$', track_open, name='track_open'),
]