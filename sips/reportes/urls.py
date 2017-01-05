from django.conf.urls import url

from reportes.views import reports_view, export_asuntos_nuevos_csv

urlpatterns = [
    url(r'lista/$', reports_view, name='listado_reportes'),
    url(r'reporte1_csv/$', export_asuntos_nuevos_csv, name='reporte1_csv'),
]
