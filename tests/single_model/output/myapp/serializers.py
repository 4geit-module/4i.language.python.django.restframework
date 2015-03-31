# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

from rest_framework import serializers
from . import models

class MyClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MyClass
        fields = ( 'title', )


