from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from cotetra.network.models import Line, Station
from cotetra.network.views import LineView
from cotetra.survey.models import Journey, Connection
from cotetra.survey.forms import JourneyForm
from tastypie.api import Api
from cotetra.network.api import StationResource, LineResource
from cotetra.survey.api import JourneyResource, ConnectionResource

admin.autodiscover()

# Implement API version 1                                                                                
v1_api = Api(api_name='v1')
# Register Shows                  
v1_api.register(LineResource())                                                                       
v1_api.register(StationResource())
v1_api.register(JourneyResource())
v1_api.register(ConnectionResource())


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^station/(?P<pk>\d+)/$', DetailView.as_view(model=Station), name="station_detail"),
    url(r'^station/$', ListView.as_view(model=Station), name="stations"),
    url(r'^line/(?P<pk>\d+)/$', LineView.as_view(), name="line_detail"),
    url(r'^line/$', ListView.as_view(model=Line)),
    url(r'^journey/$', ListView.as_view(model=Journey)),
    url(r'^journey/new/$', CreateView.as_view(model=Journey, 
                                             form_class=JourneyForm, 
                                             success_url="/journey/"), name="journey_new"),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^api/', include(v1_api.urls)),
)
