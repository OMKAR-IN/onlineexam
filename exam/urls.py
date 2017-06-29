from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^exam/$', views.tests_list),
]
