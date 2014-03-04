# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Rodolphe Quiédeville <rodolphe@quiedeville.org>
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
from django.contrib import admin
from cotetra.survey.models import Journey, Connection


class JourneyAdmin(admin.ModelAdmin):
    """Custom Admin for Journey
    """
    list_display = ('station_from', 'station_to')
    list_filter = ('station_from', 'station_to')


class ConnectionAdmin(admin.ModelAdmin):
    """Custom Admin for Connection
    """
    list_display = ('station_from', 'station_to')
    list_filter = ('station_from', 'station_to')


admin.site.register(Journey, JourneyAdmin)
admin.site.register(Connection, ConnectionAdmin)

