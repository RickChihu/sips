from django.contrib import admin

# Register your models here.
from asuntos.models import Tipo, Asunto

admin.site.register(Tipo)
admin.site.register(Asunto)