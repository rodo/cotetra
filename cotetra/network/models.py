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
from django.contrib.auth.models import User


class Line(models.Model):
    """
    A resume
    """
    name = models.CharField(max_length=300,
                            verbose_name='Name')

    ref = models.CharField(max_length=300,
                            verbose_name='Ref')

    operator = models.CharField(max_length=300,
                                verbose_name='Operator')

    wheelchair = models.CharField(max_length=300,
                                  verbose_name='Wheelchair',
                                  blank=True,
                                  null=True)

    line = models.CharField(max_length=30,
                            verbose_name='Line')

    colour = models.CharField(max_length=10, 
                              editable='False',
                              blank=True,
                              null=True)

    osmid = models.IntegerField()

    tags = models.CharField(max_length=3000,
                            verbose_name='Tags')
    


    def __unicode__(self):
        """The unicode method
        """
        return u'%s' % (self.name)


class Station(models.Model):
    """
    A resume
    """
    name = models.CharField(max_length=300,
                            verbose_name='Name')

    station = models.CharField(max_length=300)

    railway = models.CharField(max_length=300)

    line = models.ManyToManyField(Line)

    osmid = models.IntegerField()

    tags = models.CharField(max_length=3000,
                            verbose_name='Tags')

    def __unicode__(self):
        """The unicode method
        """
        return u'%s' % (self.name)
