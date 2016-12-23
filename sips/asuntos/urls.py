from django.conf.urls import url

from asuntos.views import CreateAsuntoView, AsuntosListView

urlpatterns = [
    url(r'crear/$', CreateAsuntoView.as_view(), name='crear_asunto'),
    url(r'listado/$', AsuntosListView.as_view(), name='listado_asuntos'),
]
