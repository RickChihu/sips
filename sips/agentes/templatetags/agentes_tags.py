from django import template

from asuntos.models import Asunto

register = template.Library()


@register.filter(name='total_asuntos')
def total_asuntos(user):
    return Asunto.objects.filter(agente_social=user).count()


@register.filter(name='total_atendidos')
def total_atendidos(user):
    return Asunto.objects.filter(agente_social=user, status='atendido').count()


@register.filter(name='total_no_atendidos')
def total_no_atendidos(user):
    return Asunto.objects.filter(agente_social=user, status='no_atendido').count()


@register.filter(name='total_en_proceso')
def total_en_proceso(user):
    return Asunto.objects.filter(agente_social=user, status='en_proceso').count()
