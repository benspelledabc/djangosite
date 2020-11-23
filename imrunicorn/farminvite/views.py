import json
import os
from datetime import datetime
from django.conf import settings
from django.db.models import Q
from django.db.models import F, ExpressionWrapper
from django.http import JsonResponse
from django.shortcuts import render
from model_utils.models import now
from .forms import InviteListingForm
from .models import InviteListing
from announcements.get_news import get_news, get_version_json, get_restart_notice
from imrunicorn.functions import step_hit_count_by_page

# Create your views here.
def unused_json_farm_invites_view(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        'body': 'no body to share',
        'header': 'farm invites view',
    }
    return JsonResponse(context)


def unused_page_farm_invites_view(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Coming Soon",
        "blurb": "This page is a place holder for what's to come soon.",
        # "blurb": get_page_blurb_override('news/'),
        "table_data": 'Shake it like it\'s going out of style!',
        "copy_year": datetime.now().year
    }
    return render(request, "farminvite/coming_soon.html", context)


def page_farm_invites_view(request):
    step_hit_count_by_page(request.path)
    # all_invites = InviteListing.objects.all().order_by('Invite_Date', 'Invite_Secondary')
    this_moment = datetime.now()
    # only events not past, ordered by date, am then pm.. then secondary listings
    all_invites = InviteListing.objects.filter(
        Q(Show_Listing=True) &
        Q(Cancel_Code="InviteActive") &
        (Q(Invite_Date=this_moment.date()) |
         Q(Invite_Date__gt=this_moment.date()))).order_by('Invite_Date', 'Invite_Secondary', 'Desired_Time_Slot', )

    context = {
        "restart": get_restart_notice,
        'contact_good': 'COMPLETE',
        'contact_okay': '85%',
        'contact_poor': '66%',
        'contact_bad': '5%',
        'release': get_version_json(),
        "title": "Farm Range Invites",
        "blurb": "Pay attention to the registration completion grade. If the only way to reach you is via MDShooters"
                 "forms or work chat you are at risk of having your invite retracted to make room for someone else "
                 "that I can communicate with. "
                 "Your invite registration completion will update as the additional info is entered into the "
                 "system.<br /><br /> "
                 "66% is fine, higher is better/easier."
                 "<li>COMPLETE - I have Phone and email to reach you.</li>"
                 "<li>85% - I have your phone number to reach you.</li>"
                 "<li>66% - I have your email to reach you.</li>"
                 "<li>5% - <i>You're at risk of being removed from "
                 "the invites.</i></li> "
                 ""
        ,
        'all_invites': all_invites,
        "copy_year": datetime.now().year
        # "copy_year": all_loads.prod
    }
    return render(request, "farminvite/calendar_list.html", context)


def page_farm_invites_view_lkg(request):
    step_hit_count_by_page(request.path)
    # all_invites = InviteListing.objects.all().order_by('Invite_Date', 'Invite_Secondary')
    this_moment = datetime.now()
    # only events not past, ordered by date, am then pm.. then secondary listings
    all_invites = InviteListing.objects.filter(
        Q(Show_Listing=True) &
        Q(Cancel_Code="InviteActive") &
        (Q(Invite_Date=this_moment.date()) |
         Q(Invite_Date__gt=this_moment.date()))).order_by('Invite_Date', 'Invite_Secondary', 'Desired_Time_Slot', )

    context = {
        "restart": get_restart_notice,
        'contact_good': 'COMPLETE',
        'contact_okay': '85%',
        'contact_poor': '66%',
        'contact_bad': '5%',
        'release': get_version_json(),
        "title": "Farm Range Invites",
        "blurb": "Pay attention to the registration completion grade. If the only way to reach you is via MDShooters_LKG "
                 "forms or work chat you are at risk of having your invite retracted to make room for someone else "
                 "that I can communicate with. "
                 "Your invite registration completion will update as the additional info is entered into the "
                 "system.<br /><br /> "
                 "66% is fine, higher is better/easier."
                 "<li>COMPLETE - I have Phone and email to reach you.</li>"
                 "<li>85% - I have your phone number to reach you.</li>"
                 "<li>66% - I have your email to reach you.</li>"
                 "<li>5% - I only have MDShooters_LKG or work chat to reach you. <i>You're at risk of being removed from "
                 "the invites.</i></li> "
                 ""
        ,
        'all_invites': all_invites,
        "copy_year": datetime.now().year
        # "copy_year": all_loads.prod
    }
    return render(request, "farminvite/calendar_list.html", context)


def page_farm_invites_view_hidden_listings(request):
    step_hit_count_by_page(request.path)
    # all_invites = InviteListing.objects.all().order_by('Invite_Date', 'Invite_Secondary')
    this_moment = datetime.now()
    # only events not past, ordered by date, am then pm.. then secondary listings
    all_invites = InviteListing.objects.filter(
        Q(Show_Listing=False) &
        (Q(Invite_Date=this_moment.date()) |
         Q(Invite_Date__gt=this_moment.date()))).order_by('Invite_Date', 'Invite_Secondary', 'Desired_Time_Slot', )

    context = {
        "restart": get_restart_notice,
        'contact_good': 'COMPLETE',
        'contact_okay': '85%',
        'contact_poor': '66%',
        'contact_bad': '5%',
        'release': get_version_json(),
        "title": "Invites Pending",
        # "blurb": "no blurb",
        'all_invites': all_invites,
        "copy_year": datetime.now().year
    }
    return render(request, "farminvite/calendar_list.html", context)


def page_farm_invites_map(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Farm Invite: Map",
        "table_data": 'Shake it like it\'s going out of style!',
        "copy_year": datetime.now().year
    }
    return render(request, "farminvite/farm_map.html", context)


def page_farm_invites_map_fake(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Coming Soon",
        "blurb": "This page is a place holder for what's to come soon.",
        "table_data": 'Shake it like it\'s going out of style!',
        "copy_year": datetime.now().year
    }
    return render(request, "farminvite/fake_map.html", context)


def page_farm_check_list(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "What should I bring?",
        "blurb": "Pre-pack your car/truck it helps to prevent forgetting things.",
        "copy_year": datetime.now().year
    }
    return render(request, "farminvite/what_to_bring.html", context)


def page_request_slot(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Request Slot",
        "blurb": "Email Me To Request Slot",
        "table_data": 'The email must contain these items or I\'ll ignore the request. I\'ll add you to the secondary '
                      'listing if primary is full. '
                      '<li>FirstName (so i dont call you dude/woman all day):</li>'
                      '<li>Display Name (MDShoters name or something else. This is what\'s displayed on the listing '
                      'page.):</li> '
                      '<li>Phone Number:</li>'
                      '<li>E-Mail:</li>'
                      '<li>Date Of Invite Requesting:</li>'
                      '<li>AM or PM</li>'                      
                      '<li><i>EMAIL SUBJECT: Aim Small Miss Small</i> (other subjects will be ignored)</li>'
                      '<li>My Address: <a href="mailto:Admin@BenSpelledABC.me">Admin@BenSpelledABC.me</a></li>'
                      ''
        ,
        "copy_year": datetime.now().year
    }
    return render(request, "farminvite/simple_use_variables.html", context)


def page_cash_app(request):
    step_hit_count_by_page(request.path)
    # return HttpResponse("Hello world 500.")
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Donate: Cash App",
        "blurb": "Cash app is our preferred method of payment.",
        "full_body": "",
        "copy_year": datetime.now().year
    }
    return render(request, "farminvite/donate_cash_app.html", context)


def page_how_to_sign_up(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "How to sign up",
        "blurb": "The process has changed!",
        "cash_app": "Show_QR_Code",
        "copy_year": datetime.now().year
    }
    return render(request, "farminvite/sign_up_how.html", context)


def page_missing_contact_info(request):
    step_hit_count_by_page(request.path)
    this_moment = datetime.now()
    # only events not past, ordered by date, am then pm.. then secondary listings
    all_invites = InviteListing.objects.filter(
        Q(Invite_Date=this_moment.date()) |
        Q(Invite_Date__gt=this_moment.date())).order_by('Invite_Date', 'Invite_Secondary', 'Desired_Time_Slot', )

    context = {
        # "roll_list": queryset,
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Registration Completion Guideline",
        "blurb": "Please provide some contact info if you show up on this list as having it missing. Failure to do so "
                 "will result in your name being removed from the invite list to make room for people that I can get "
                 "in touch with. Entries without at least one or the other will be removed five days before the event "
                 "and the invite will be "
                 "sent to the secondary person for that day.<br /><br />"
                 "I don't need both email and phone but it makes life much easier to have a phone listed on file. My "
                 "cellphone service isn't great at the farm and I might not be able to email you. The text messages "
                 "on the other hand will go thru, eventually.<br /><br />"
                 "Your invite registration completion will update as the additional info is entered into the system."
                 ""
        ,
        'all_invites': all_invites,
        "copy_year": datetime.now().year
    }
    return render(request, "farminvite/missing_contact_info.html", context)


def page_invite_listing(request):
    step_hit_count_by_page(request.path)
    if request.method == 'POST':
        form = InviteListingForm(request.POST)
        if form.is_valid():
            print("VALID")
            form.save()

    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        'form': InviteListingForm(),
        "copy_year": datetime.now().year
    }

    return render(request, 'farminvite/invite_listing_form.html', context)

