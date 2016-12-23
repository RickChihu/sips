from django.contrib.auth.models import User
from django.views.generic.list import ListView

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
