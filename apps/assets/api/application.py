#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from rest_framework_bulk import BulkModelViewSet

from ..models import Application
from .. import serializers


__all__ = [
    'ApplicationViewSet',
]


class ApplicationViewSet(BulkModelViewSet):
    queryset = Application.objects.all()
    serializer_class = serializers.ApplicationSerializer
