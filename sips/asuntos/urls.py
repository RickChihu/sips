from django.conf.urls import url

from asuntos.views import CreateAsuntoView, AsuntosListView, asignar_agente, CreateAsuntoEventoView, \
    AsuntoEventosListView, cambiar_status

urlpatterns = [
    url(r'crear/$', CreateAsuntoView.as_view(), name='crear_asunto'),
    url(r'listado/$', AsuntosListView.as_view(), name='listado_asuntos'),
    url(r'asignar-agente/(?P<pk>[0-9]+)/$', asignar_agente, name='asignar_agente'),
    url(r'crear-evento/(?P<pk>[0-9]+)/$', CreateAsuntoEventoView.as_view(), name='crear_asunto_evento'),
    url(r'listado-eventos/(?P<pk>[0-9]+)/$', AsuntoEventosListView.as_view(), name='listado_eventos'),
    url(r'cambiar-status/(?P<pk>[0-9]+)/$', cambiar_status, name='cambiar_status'),
]
