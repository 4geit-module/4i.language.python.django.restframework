# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

from myapp import views as myapp_views
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, DetailView, ListView
from . import models, views

