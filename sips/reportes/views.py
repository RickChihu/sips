import csv

from django.shortcuts import render
from django.http import HttpResponse

from asuntos.models import Asunto


def reports_view(request):
    return render(request, 'reportes/listado.html', {})


def export_asuntos_nuevos_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Asunto', 'Folio', 'Nombre', 'Curp', 'Domicilio'])

    asuntos = Asunto.objects.all()
    for asunto in asuntos:
        writer.writerow(asunto)

    return response
