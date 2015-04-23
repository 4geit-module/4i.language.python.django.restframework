# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.contenttypes.models import ContentType

class MyClass(models.Model):
    """
    MyClass
        
    :param title: 
    :type title: char
    """

    title = models.CharField(_('title'), max_length=200)

    def save(self, *args, **kwargs):
        super(MyClass, self).save(*args, **kwargs)

    def __unicode__(self):
        return """MyClass (%d)""" % self.id

