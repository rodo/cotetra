# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 Rodolphe Quiédeville <rodolphe@quiedeville.org>
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
Models definition for resume
"""
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse


class Stop(models.Model):
    """
    """
    name = models.CharField(max_length=300,
                            verbose_name='Name')

    description = models.CharField(max_length=300,
                                   verbose_name='Description')

    lon = models.FloatField(default=0)
    lat = models.FloatField(default=0)

    def __unicode__(self):
        """The unicode method
        """
        return u'%s' % (self.name)


class Route(models.Model):
    """
    """
    name = models.CharField(max_length=300,
                            verbose_name='Name')

    description = models.CharField(max_length=300,
                                   verbose_name='Description')
    
    def __unicode__(self):
        """The unicode method
        """
        return u'%s' % (self.name)


class Trip(models.Model):
    """
    """
    route = models.ForeignKey(Route, verbose_name='Route')
    service = models.IntegerField(verbose_name='Service')
    direction = models.PositiveSmallIntegerField()

    def __unicode__(self):
        """The unicode method
        """
        return u'%s %s' % (self.pk, self.route)


class StopTime(models.Model):
    """
    """
    stop = models.ForeignKey(Stop)
    trip = models.ForeignKey(Trip)

    sequence = models.PositiveSmallIntegerField()

    def __unicode__(self):
        """The unicode method
        """
        return u'%s' % (self.stop)


class Transfer(models.Model):
    """
    """
    from_stop = models.IntegerField()
    to_stop = models.IntegerField()
    transfer_type = models.PositiveSmallIntegerField()

    #  Time in seconds
    seconds = models.PositiveSmallIntegerField()

    def __unicode__(self):
        """The unicode method
        """
        return u'%s %s' % (self.from_stop, self.to_stop)
