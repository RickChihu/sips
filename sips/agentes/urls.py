from django.conf.urls import url

from agentes.views import AgentesListView

urlpatterns = [
    url(r'listado/$', AgentesListView.as_view(), name='listado_agentes'),
]
