import json,os,requests
import os
from datetime import datetime
from django.conf import settings
from django.db.models import Q
from django.db.models import F, ExpressionWrapper
from django.http import JsonResponse
from django.shortcuts import render
from model_utils.models import now
from subprocess import Popen, PIPE, STDOUT
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from announcements.get_news import get_news, get_version_json, get_page_blurb_override, get_restart_notice
from imrunicorn.functions import step_hit_count_by_page


# Create your views here.
def admintool_restart_gunicorn(request):
    step_hit_count_by_page(request.path)
    command = ["bash", "admin_toolbox/server_control.sh", "restart_gunicorn"]
    try:
        process = Popen(command, stdout=PIPE, stderr=STDOUT)
        output = process.stdout.read()
        exit_status = process.poll()
        result = {}

        if exit_status == 0:
            result = {"status": "Success", "output": str(output)}
            # return JsonResponse({"status": "Success", "output": str(output)})
        else:
            result = {"status": "Failed", "output": str(output)}
            # return JsonResponse({"status": "Failed", "output": str(output)})
    except Exception as e:
        result = {"status": "failed", "output": str(e)}
        # return JsonResponse({"status": "failed", "output": str(e)})

    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "AdminTool: Restart Gunicorn",
        # "blurb": "I moved the calculator to its own page.",
        "blurb": get_page_blurb_override('admin_tool/restart_gunicorn/'),
        "copy_year": datetime.now().year,
        "table_data": result,
    }
    return render(request, "admin_toolbox/output.html", context)


def admintool_restart_nginx(request):
    step_hit_count_by_page(request.path)
    command = ["bash", "admin_toolbox/server_control.sh", "restart_nginx"]
    try:
        process = Popen(command, stdout=PIPE, stderr=STDOUT)
        output = process.stdout.read()
        exit_status = process.poll()
        result = {}

        if exit_status == 0:
            result = {"status": "Success", "output": str(output)}
            # return JsonResponse({"status": "Success", "output": str(output)})
        else:
            result = {"status": "Failed", "output": str(output)}
            # return JsonResponse({"status": "Failed", "output": str(output)})
    except Exception as e:
        result = {"status": "failed", "output": str(e)}
        # return JsonResponse({"status": "failed", "output": str(e)})

    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "AdminTool: Restart Nginx",
        # "blurb": "I moved the calculator to its own page.",
        "blurb": get_page_blurb_override('admin_tool/restart_nginx/'),
        "copy_year": datetime.now().year,
        "table_data": result,
    }
    return render(request, "admin_toolbox/output.html", context)


def admintool_restart_gunicorn_and_nginx(request):
    step_hit_count_by_page(request.path)
    command = ["bash", "admin_toolbox/server_control.sh", "restart_gunicorn_and_nginx"]
    try:
        process = Popen(command, stdout=PIPE, stderr=STDOUT)
        output = process.stdout.read()
        exit_status = process.poll()
        result = {}

        if exit_status == 0:
            result = {"status": "Success", "output": str(output)}
            # return JsonResponse({"status": "Success", "output": str(output)})
        else:
            result = {"status": "Failed", "output": str(output)}
            # return JsonResponse({"status": "Failed", "output": str(output)})
    except Exception as e:
        result = {"status": "failed", "output": str(e)}
        # return JsonResponse({"status": "failed", "output": str(e)})

    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "AdminTool: Restart Gunicorn & Nginx",
        # "blurb": "I moved the calculator to its own page.",
        "blurb": get_page_blurb_override('admin_tool/restart_gunicorn_and_nginx/'),
        "copy_year": datetime.now().year,
        "table_data": result,
    }
    return render(request, "admin_toolbox/output.html", context)


def admintool_cancel_restarts(request):
    step_hit_count_by_page(request.path)
    command = ["bash", "admin_toolbox/server_control.sh", "cancel_all_restarts"]
    try:
        process = Popen(command, stdout=PIPE, stderr=STDOUT)
        output = process.stdout.read()
        exit_status = process.poll()
        result = {}

        if exit_status == 0:
            result = {"status": "Success", "output": str(output)}
            # return JsonResponse({"status": "Success", "output": str(output)})
        else:
            result = {"status": "Failed", "output": str(output)}
            # return JsonResponse({"status": "Failed", "output": str(output)})
    except Exception as e:
        result = {"status": "failed", "output": str(e)}
        # return JsonResponse({"status": "failed", "output": str(e)})

    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "AdminTool: Cancel All Restarts",
        # "blurb": "I moved the calculator to its own page.",
        "blurb": get_page_blurb_override('admin_tool/cancel_all_restarts/'),
        "copy_year": datetime.now().year,
        "table_data": result,
    }
    return render(request, "admin_toolbox/output.html", context)


def dir_maker(request):
    step_hit_count_by_page(request.path)
    command = ["bash", "admin_toolbox/dir_maker.sh", "create"]
    try:
        process = Popen(command, stdout=PIPE, stderr=STDOUT)
        output = process.stdout.read()
        exit_status = process.poll()

        if exit_status == 0:
            return JsonResponse({"status": "Success", "output": str(output)})
        else:
            return JsonResponse({"status": "Failed", "output": str(output)})
    except Exception as e:
        return JsonResponse({"status": "failed", "output": str(e)})


def dir_delete(request):
    step_hit_count_by_page(request.path)
    command = ["bash", "admin_toolbox/dir_maker.sh", "delete"]
    try:
        process = Popen(command, stdout=PIPE, stderr=STDOUT)
        output = process.stdout.read()
        exit_status = process.poll()

        if exit_status == 0:
            return JsonResponse({"status": "Success", "output": str(output)})
        else:
            return JsonResponse({"status": "Failed", "output": str(output)})
    except Exception as e:
        return JsonResponse({"status": "failed", "output": str(e)})


#
# @csrf_exempt
# def file_maniputer(request):
#     if request.method == 'POST':
#         request_data = json.loads(request.body)
#         if request_data["action"] == "create":
#             data = dir_maker()
#         else:
#             data = {"status": "not defined", "output": "not defined"}
#
#         response = HttpResponse(json.dumps(data), content_type='application/json', status=200)
#         return response


def no_request_found(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        'body': 'no_request_found',
        'header': 'no_request_found view',
    }
    return JsonResponse(context)
