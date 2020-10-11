from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('greyscale_test')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_groups(allowed_groupname_list=['']):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.filter(name__in=allowed_groupname_list).exists():
                return view_func(request, *args, **kwargs)
            else:
                # return HttpResponse("You are not authorized to view this page. Check your groups and try again.")
                return redirect('access_denied_groups')

        return wrapper_func
    return decorator
