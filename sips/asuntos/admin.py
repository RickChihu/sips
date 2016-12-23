from django.contrib import admin

from asuntos.models import Tipo, Asunto, Municipio

admin.site.register(Tipo)
admin.site.register(Asunto)
admin.site.register(Municipio)
