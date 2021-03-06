from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from asuntos.forms import AsuntoEventoForm
from asuntos.models import Asunto, AsuntoEvento
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

        if self.request.user.groups.filter(name__in=[AGENTE_SOCIAL]):
            now = datetime.today()
            one_week_later = now + timedelta(days=7)

            queryset = AsuntoEvento.objects.filter(
                asunto__agente_social=self.request.user,
                fecha_visita_juzgado__gte=now,
                fecha_visita_juzgado__lte=one_week_later
            ).order_by('fecha_visita_juzgado')

            self.request.session['alertas'] = [{'asunto': x.asunto.asunto.name,
                                                'folio': x.asunto.folio_(),
                                                'fecha': x.fecha_visita_juzgado.strftime("%Y-%m-%d %H:%M"),
                                                'juzgado': x.juzgado} for x in queryset]

        return context

    def get_queryset(self):
        if self.request.user.groups.filter(name__in=[AGENTE_SOCIAL]):
            queryset = Asunto.objects.filter(agente_social=self.request.user).order_by('-id')
        else:
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


class CreateAsuntoEventoView(CreateView):
    form_class = AsuntoEventoForm
    template_name = 'asuntos/asunto_evento_form.html'
    success_url = reverse_lazy('listado_asuntos')

    def get_context_data(self, **kwargs):
        context = super(CreateAsuntoEventoView, self).get_context_data(**kwargs)
        return context

    def get_initial(self):
        asunto = get_object_or_404(Asunto, pk=self.kwargs.get('pk'))
        return {'asunto': asunto}

    def form_valid(self, form):
        evento = form.save(commit=False)
        asunto = get_object_or_404(Asunto, pk=self.kwargs.get('pk'))
        evento.asunto = asunto
        evento.save()
        return super(CreateAsuntoEventoView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('listado_eventos', kwargs={'pk': self.kwargs['pk']})


class AsuntoEventosListView(ListView):
    model = AsuntoEvento
    paginate_by = 50
    template_name = 'asuntos/listado_eventos.html'

    def get_context_data(self, **kwargs):
        context = super(AsuntoEventosListView, self).get_context_data(**kwargs)
        context['asunto'] = get_object_or_404(Asunto, pk=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        queryset = AsuntoEvento.objects.filter(asunto=get_object_or_404(Asunto, pk=self.kwargs.get('pk'))).order_by('-id')
        return queryset


def cambiar_status(request, pk):
    asunto = get_object_or_404(Asunto, pk=pk)

    if request.method == 'GET':
        status = request.GET.get('status')
        asunto.status = status
        asunto.save()

        return redirect(reverse('listado_asuntos'))
