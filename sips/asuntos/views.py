from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from asuntos.models import Asunto


class CreateAsuntoView(CreateView):
    model = Asunto
    fields = ['nombre', 'curp', 'domicilio', 'colonia', 'asunto', 'competencia_ps']
    template_name = 'asuntos/asunto_form.html'
    success_url = reverse_lazy('listado_asuntos')

    def get_context_data(self, **kwargs):
        context = super(CreateAsuntoView, self).get_context_data(**kwargs)
        return context


class AsuntosListView(ListView):
    model = Asunto
    paginate_by = 50
    template_name = 'asuntos/listado.html'

    def get_context_data(self, **kwargs):
        context = super(AsuntosListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        queryset = Asunto.objects.all().order_by('-id')
        return queryset