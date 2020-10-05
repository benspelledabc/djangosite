from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            # return redirect('home')
            return redirect('greyscale_test')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_groups(allowed_group_list=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            allowed = False

            if request.user.groups.exists():
                user_group_list = request.user.groups.all()
                print("Group List:", user_group_list)

                for group_name in user_group_list:
                    print("group_name:", group_name)
                    if group_name in allowed_group_list:
                        allowed = True

            if allowed:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page.")

            # print("Working:", allowed_group_list)

        return wrapper_func
    return decorator


# only allows user in 1 group at a time because of index location usage.
def allowed_groups_bad(allowed_group_list=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_group_list:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page.")

            # print("Working:", allowed_group_list)

        return wrapper_func
    return decorator
