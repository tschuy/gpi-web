from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    '',
    url(r'^package/(?P<name>[^/]+)/?$',
        'gpi.gpi_web.views.project_details',
        name='package-details'),
)
