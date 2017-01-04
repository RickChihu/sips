from django.conf.urls import url

from blog.views import CreateEntryView, EntryListView, EditEntryView

urlpatterns = [
    url(r'crear/$', CreateEntryView.as_view(), name='crear_entry'),
    url(r'listado/$', EntryListView.as_view(), name='listado_entries'),
    url(r'editar/(?P<pk>[0-9]+)/$', EditEntryView.as_view(), name='editar_entry'),
]
