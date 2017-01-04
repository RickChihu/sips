from django.conf.urls import url

from asuntos.views import CreateAsuntoView, AsuntosListView, asignar_agente, CreateAsuntoEventoView

urlpatterns = [
    url(r'crear/$', CreateAsuntoView.as_view(), name='crear_asunto'),
    url(r'listado/$', AsuntosListView.as_view(), name='listado_asuntos'),
    url(r'asignar-agente/(?P<pk>[0-9]+)/$', asignar_agente, name='asignar_agente'),
    url(r'crear-evento/$', CreateAsuntoEventoView.as_view(), name='crear_asunto_evento'),
]
