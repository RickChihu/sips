from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.views.generic.list import ListView

from asuntos.models import AsuntoEvento
from utils.constants import AGENTE_SOCIAL


class AgentesListView(ListView):
    model = User
    paginate_by = 50
    template_name = 'agentes/listado.html'

    def get_context_data(self, **kwargs):
        context = super(AgentesListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        queryset = User.objects.filter(groups__name__in=[AGENTE_SOCIAL])
        return queryset


class AgendaListView(ListView):
    model = AsuntoEvento
    paginate_by = 50
    template_name = 'agentes/agenda.html'

    def get_context_data(self, **kwargs):
        context = super(AgendaListView, self).get_context_data(**kwargs)
        now = datetime.today()

        context['historic'] = AsuntoEvento.objects.filter(
            asunto__agente_social=self.request.user,
            fecha_visita_juzgado__lte=now
        ).order_by('fecha_visita_juzgado')

        return context

    def get_queryset(self):
        now = datetime.today()
        one_week_later = now + timedelta(days=7)

        queryset = AsuntoEvento.objects.filter(
            asunto__agente_social=self.request.user,
            fecha_visita_juzgado__gte=now,
            fecha_visita_juzgado__lte=one_week_later
        ).order_by('fecha_visita_juzgado')
        return queryset
