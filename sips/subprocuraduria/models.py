from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Subprocuraduria(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    usuarios = models.ManyToManyField(User)

    def __unicode__(self):
        return '%s' % self.nombre


class Direccion(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    subprocuraduria = models.ForeignKey(Subprocuraduria)
    usuarios = models.ManyToManyField(User)

    def __unicode__(self):
        return '%s' % self.nombre
