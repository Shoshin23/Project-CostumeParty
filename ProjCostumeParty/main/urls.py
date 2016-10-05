from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$',views.load_map, name='load_map'),
# url(r'^post/new/$', views.post_new, name='post_new'),
]
