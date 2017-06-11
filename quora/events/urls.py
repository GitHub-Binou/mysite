from django.conf.urls import url
from quora.events.views import (
    edit,
    events,
    event,
    write,
)

urlpatterns = [
    url(r'^$', events, name='events'),
    url(r'^write/$', write, name='write_event'),
    url(r'^edit/(?P<id>\d+)/$', edit, name='edit_event'),
    url(r'^(?P<id>\d+)/$', event, name='event'),
]
