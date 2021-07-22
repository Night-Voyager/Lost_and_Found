from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api-test/$', views.Test.as_view())
]
