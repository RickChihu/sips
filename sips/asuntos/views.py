from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from asuntos.models import Asunto
from utils.constants import AGENTE_SOCIAL


class CreateAsuntoView(CreateView):
    model = Asunto
    fields = ['nombre', 'curp', 'domicilio', 'colonia', 'municipio', 'asunto', 'competencia_ps']
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


def asignar_agente(request, pk):
    asunto = get_object_or_404(Asunto, pk=pk)

    if request.method == 'GET':
        agentes = User.objects.filter(groups__name__in=[AGENTE_SOCIAL])
        return render(request, 'asuntos/asignar-agente.html', {'asunto': asunto, 'agentes': agentes})

    elif request.method == 'POST':
        agente = User.objects.get(pk=request.POST.get('agente', ''))
        asunto.agente_social = agente
        asunto.status = 'en_proceso'
        asunto.save()

        return redirect(reverse('listado_asuntos'))