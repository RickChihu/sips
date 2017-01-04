import uuid

from django.contrib.auth.models import User
from django.db import models

STATUS_CHOICES = (
    ('atendido', 'Atendido'),
    ('no_atendido', 'No Atendido'),
    ('en_proceso', 'En Proceso'),
)


class Municipio(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __unicode__(self):
        return '%s' % self.name


class Tipo(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __unicode__(self):
        return '%s' % self.name


class Asunto(models.Model):
    folio = models.UUIDField(default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    curp = models.CharField(max_length=100, blank=False, null=False)
    domicilio = models.CharField(max_length=100, blank=False, null=False)
    colonia = models.CharField(max_length=100, blank=False, null=False)
    municipio = models.ForeignKey(Municipio)
    asunto = models.ForeignKey(Tipo)
    competencia_ps = models.BooleanField('Competencia de la Procuraduria Social', default=False)
    added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, null=True, max_length=20, blank=True)
    agente_social = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.folio

    def folio_(self):
        return (str(self.folio)[:8]).upper()


class AsuntoEvento(models.Model):
    asunto = models.ForeignKey(Asunto)
    fecha_cita_usuario = models.DateTimeField(null=False)
    observaciones_cita_usuario = models.TextField(blank=True, null=False)
    fecha_visita_juzgado = models.DateTimeField(null=False)
    juzgado = models.CharField(max_length=100, blank=False, null=False)
    observaciones_visita_juzgado = models.TextField(blank=True, null=False)
