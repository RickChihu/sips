from functools import wraps

from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def has_group(group_names):
    def _check_group(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('/login/')

            if not request.user.groups.filter(name__in=group_names).exists():
                raise PermissionDenied

            return view_func(request, *args, **kwargs)
        return wrapper
    return _check_group
