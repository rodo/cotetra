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
from cotetra.network.models import Station


class Journey(models.Model):
    """
    A Journey
    """
    station_from = models.ForeignKey(Station, related_name="jfrom")
    station_to = models.ForeignKey(Station, related_name="jto")
    duration = models.TimeField()

    def __unicode__(self):
        """The unicode method
        """
        return u"{} - {}".format(self.station_from, self.station_to)


class Connection(models.Model):
    """
    A Connection
    """
    station_from = models.ForeignKey(Station, related_name="cfrom")
    station_to = models.ForeignKey(Station, related_name="cto")
    duration = models.TimeField()

    def __unicode__(self):
        """The unicode method
        """
        return u"{} - {}".format(self.station_from, self.station_to)
