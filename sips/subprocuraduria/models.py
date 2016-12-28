from __future__ import unicode_literals

from django.db import models


class Subprocuraduria(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)

    def __unicode__(self):
        return '%s' % self.nombre


class Direccion(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    subprocuraduria = models.ForeignKey(Subprocuraduria)

    def __unicode__(self):
        return '%s' % self.nombre
