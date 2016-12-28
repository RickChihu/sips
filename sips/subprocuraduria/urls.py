from django.conf.urls import url

from subprocuraduria.views import CreateSubprocuraduriaView, CreateDireccionView, SubprocuraduriaListView, \
    DireccionListView

urlpatterns = [
    url(r'crear-subprocuraduria/$', CreateSubprocuraduriaView.as_view(), name='crear_subprocuraduria'),
    url(r'listado-subprocuradurias/$', SubprocuraduriaListView.as_view(), name='listado_subprocuradurias'),
    url(r'crear-direccion/$', CreateDireccionView.as_view(), name='crear_direccion'),
    url(r'listado-direcciones/$', DireccionListView.as_view(), name='listado_direcciones'),
]
