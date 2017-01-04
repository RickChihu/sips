from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='in_list')
def in_list(value, the_list):
    the_list = [x.strip() for x in the_list.encode('utf8').split(',')]
    return value in the_list


@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")


@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
