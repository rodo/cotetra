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

class Survey(models.Model):
    """
    A survey
    """
    station_from = models.ForeignKey(Station, related_name="from")
    station_to = models.ForeignKey(Station, related_name="to")

    time = models.TimeField()

    travel = models.IntegerField(default=0,
                                 choices=((0, 'journey'),
                                          (1, 'connection')))


    def __unicode__(self):
        """The unicode method
        """
        return u"{} - {}".format(self.station_from, self.station_to)
