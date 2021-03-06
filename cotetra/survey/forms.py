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
#
from django import forms
from django.forms.widgets import Textarea, Select, TextInput
from cotetra.survey.models import Journey, Connection


class JourneyForm(forms.ModelForm):
    """
    Use to create a new journey
    """
    class Meta:
        model = Journey


class ConnectionForm(forms.ModelForm):
    """
    Use to create a new connection
    """
    class Meta:
        model = Connection
