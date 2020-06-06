from django.conf.urls import url
from django.urls import path, include

from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^Display_Router_Details$', Display_Router, name='Display_Router'),

    url(r'^Create_router$', Create_router, name='Create_router'),

    url(r'^Update_Router/(?P<pk>\d+)$', Update_Router, name='Update_Router'),

    url(r'^Delete_Router/(?P<pk>\d+)$', Delete_Router, name='Delete_Router'),

]
