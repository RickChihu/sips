from django import template

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_names):
    if user.is_authenticated():
        group_names = [x.strip() for x in group_names.split(',')]

        return user.groups.filter(name__in=group_names).exists()

    return False
