from django.conf.urls import url
from . import views
app_name = 'states'
urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^(?P<country_name>[-w]+)/$', views.apple, name='apple'),
]