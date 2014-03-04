# -*- coding: utf-8 -*-  pylint: disable-msg=R0801
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
API definition
"""
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.throttle import BaseThrottle
from cotetra.survey.models import Journey, Connection
from cotetra.network.api import StationResource


class JourneyResource(ModelResource):
    """
    The journeys
    """
    station_from = fields.ForeignKey(StationResource, 'station_from')
    station_to = fields.ForeignKey(StationResource, 'station_to')

    class Meta:
        queryset = Journey.objects.all()
        resource_name = 'journey'
        throttle = BaseThrottle(throttle_at=100, timeframe=60)


class ConnectionResource(ModelResource):
    """
    The connections
    """
    station_from = fields.ForeignKey(StationResource, 'station_from')
    station_to = fields.ForeignKey(StationResource, 'station_to')

    class Meta:
        queryset = Connection.objects.all()
        resource_name = 'connection'
        throttle = BaseThrottle(throttle_at=100, timeframe=60)
