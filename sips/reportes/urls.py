from django.conf.urls import url

from reportes.views import reports_view, export_asuntos_nuevos_csv, export_asuntos_mes_pasado_csv, \
    export_asuntos_nuevos_word, export_asuntos_nuevos_pdf, export_asuntos_mes_pasado_word, export_asuntos_mes_pasado_pdf

urlpatterns = [
    url(r'lista/$', reports_view, name='listado_reportes'),
    url(r'reporte1_csv/$', export_asuntos_nuevos_csv, name='reporte1_csv'),
    url(r'reporte1_word/$', export_asuntos_nuevos_word, name='reporte1_word'),
    url(r'reporte1_pdf/$', export_asuntos_nuevos_pdf, name='reporte1_pdf'),
    url(r'reporte2_csv/$', export_asuntos_mes_pasado_csv, name='reporte2_csv'),
    url(r'reporte2_word/$', export_asuntos_mes_pasado_word, name='reporte2_word'),
    url(r'reporte2_pdf/$', export_asuntos_mes_pasado_pdf, name='reporte2_pdf'),
]
