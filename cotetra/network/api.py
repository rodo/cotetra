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
from tastypie.cache import SimpleCache
from tastypie.throttle import BaseThrottle
from cotetra.network.models import Station, Line


class StationResource(ModelResource):
    """
    The station
    """
    class Meta:
        queryset = Station.objects.all()
        resource_name = 'station'
        excludes = ['tags']
        throttle = BaseThrottle(throttle_at=100, timeframe=60)
        cache = SimpleCache()


class LineResource(ModelResource):
    """
    The line
    """
    class Meta:
        queryset = Line.objects.all()
        resource_name = 'line'
        excludes = ['tags']
        throttle = BaseThrottle(throttle_at=100, timeframe=60)
        cache = SimpleCache()
