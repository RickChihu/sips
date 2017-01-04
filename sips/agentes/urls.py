from django.conf.urls import url

from agentes.views import AgentesListView, AgendaListView

urlpatterns = [
    url(r'listado/$', AgentesListView.as_view(), name='listado_agentes'),
    url(r'agenda/$', AgendaListView.as_view(), name='agenda'),
]
