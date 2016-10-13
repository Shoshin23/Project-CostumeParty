from django.conf.urls import url, include
from . import views

urlpatterns = [
url(r'^$',views.load_map, name='load_map'),
url(r'^search/', include('haystack.urls')),
]
