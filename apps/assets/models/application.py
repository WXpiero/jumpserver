#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _

from orgs.mixins import OrgModelMixin
from common.fields.model import JsonDictTextField

__all__ = ['Application']


class Application(OrgModelMixin):

    TYPE_CHROME = 'chrome'
    TYPE_CHOICES = (
        (TYPE_CHROME, 'Chrome'),
    )

    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True
    )
    name = models.CharField(
        max_length=128, verbose_name=_('Name')
    )
    asset = models.ForeignKey(
        'assets.Asset', on_delete=models.CASCADE, verbose_name=_('Asset')
    )
    system_user = models.ForeignKey(
        'assets.SystemUser', on_delete=models.CASCADE, verbose_name=_('System user')
    )
    app_type = models.CharField(
        max_length=128, choices=TYPE_CHOICES, verbose_name=_('Type')
    )
    params = JsonDictTextField(
        max_length=4096, blank=True, null=True, verbose_name=_('Params')
    )
    created_by = models.CharField(
        max_length=32, null=True, blank=True, verbose_name=_('Created by')
    )
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name=_('Date created')
    )
    comment = models.TextField(
        max_length=128, default='', blank=True, verbose_name=_('Comment')
    )

    class Meta:
        unique_together = [('org_id', 'name')]
        verbose_name = _("Application")

    def __str__(self):
        return self.name
