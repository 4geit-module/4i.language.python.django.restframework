# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

from rest_framework import viewsets
from . import serializers
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views import generic
from . import models, forms

class MyClassViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows myclasss to be viewed or edited.
    """
    queryset = models.MyClass.objects.all()
    serializer_class = serializers.MyClassSerializer


