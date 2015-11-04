# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function


from django.db import models
from django.utils.translation import ugettext_lazy as _


class Parameter(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, null=True, blank=True)
    formula_allowed = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.id
    

class ScadaSource(models.Model):
    """Scada. """
    SCADA_CSV = 'CSV'
    SCADA_PIXML = 'PIXML'
    SCADA_MON = 'MON'
    SOURCE_CHOICES = (
        (SCADA_CSV, 'Scada csv'),
        (SCADA_PIXML, 'Scada pixml'),
        (SCADA_MON, 'Scada mon')
    )
    name = models.CharField(primary_key=True, max_length=255)
    directory = models.CharField(max_length=255, null=True, blank=True)
    source_type = models.CharField(max_length=50, choices=SOURCE_CHOICES)

    def __unicode__(self):
        return "{0} | {1}".format(self.name, self.directory) 
    
    class Meta:
        ordering = ['name']


class ScadaLocation(models.Model):
    """Location from scada."""

    locationid = models.CharField(primary_key=True, max_length=100)
    locationname = models.CharField(max_length=255, null=True, blank=True)
    source = models.ForeignKey(ScadaSource, null=True, blank=True)

    def __unicode__(self):
        if self.locationname is None:
            return self.locationid
        else:
            return self.locationname

    class Meta:
        ordering = ['locationname']


class Header(models.Model):
    """Locations, parameter from scada."""
    location = models.ForeignKey(ScadaLocation, related_name='headers')
    parameter = models.ForeignKey(Parameter, null=True, blank=True)
    unit = models.CharField(max_length=30, null=True, blank=True)
    begintime = models.DateTimeField(null=True, blank=True)
    endtime = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['location__locationid']
        unique_together = (('location', 'parameter'),)

    def __unicode__(self):
        parameterid = None
        if self.parameter is not None:
            parameterid = self.parameter.id
        return "{0} -- {1}".format(self.location.locationid, parameterid)
