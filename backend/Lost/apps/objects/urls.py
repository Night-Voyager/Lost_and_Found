from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^find_object/$', views.FindObjectList.as_view()),
    url(r'^find_object/(?P<pk>[0-9]+)/$', views.FindObjectDetail.as_view()),

    url(r'^find_owner/$', views.FindOwnerList.as_view()),
    url(r'^find_owner/(?P<pk>[0-9]+)/$', views.FindOwnerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

'''
url(r'^find_object/$', views.FindObjectList.as_view()),
url(r'^find_object/(?P<pk>[0-9]+)/$', views.FindObjectDetail.as_view()),
url(r'^find_owner/$', views.FindOwnerList.as_view()),
url(r'^find_owner/(?P<pk>[0-9]+)/$', views.FindOwnerDetail.as_view()),
'''

'''
url(r'^find_object/$', views.FindObjectView.as_view()),
url(r'find_owner/$', views.FindOwnerView.as_view())
'''