# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

from myapp import views as myapp_views
from rest_framework import routers
from django.conf.urls import patterns, include, url
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'myapp_myclass', myapp_views.MyClassViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xyz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^docs/', include('rest_framework_swagger.urls')),
)
