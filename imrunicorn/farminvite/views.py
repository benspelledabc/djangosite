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
from announcements.get_news import get_news, get_version_json


# Create your views here.
def unused_json_farm_invites_view(request):
    context = {
        'body': 'no body to share',
        'header': 'farm invites view',
    }
    return JsonResponse(context)


def unused_page_farm_invites_view(request):
    context = {
        'release': get_version_json(),
        "title": "Coming Soon",
        "blurb": "This page is a place holder for what's to come soon.",
        "table_data": 'Shake it like it\'s going out of style!',
        "copy_year": datetime.now().year
    }
    return render(request, "farminvite/coming_soon.html", context)


def page_farm_invites_view(request):
    # all_invites = InviteListing.objects.all().order_by('Invite_Date', 'Invite_Secondary')
    this_moment = datetime.now()
    # only events not past, ordered by date, am then pm.. then secondary listings
    all_invites = InviteListing.objects.filter(
        Q(Show_Listing=True) &
        (Q(Invite_Date=this_moment.date()) |
         Q(Invite_Date__gt=this_moment.date()))).order_by('Invite_Date', 'Invite_Secondary', 'Desired_Time_Slot', )

    context = {
        'contact_good': 'COMPLETE',
        'contact_okay': '85%',
        'contact_poor': '66%',
        'contact_bad': '5%',
        'release': get_version_json(),
        "title": "Farm Range Invites",
        "blurb": "Pay attention to the registration completion grade. If the only way to reach you is via MDShooters "
                 "forms or work chat you are at risk of having your invite retracted to make room for someone else "
                 "that I can communicate with. "
                 "Your invite registration completion will update as the additional info is entered into the "
                 "system.<br /><br /> "
                 "66% is fine, higher is better/easier."
                 "<li>COMPLETE - I have Phone and email to reach you.</li>"
                 "<li>85% - I have your phone number to reach you.</li>"
                 "<li>66% - I have your email to reach you.</li>"
                 "<li>5% - I only have MDShooters or work chat to reach you. <i>You're at risk of being removed from "
                 "the invites.</i></li> "
                 ""
        ,
        'all_invites': all_invites,
        "copy_year": datetime.now().year
        # "copy_year": all_loads.prod
    }
    return render(request, "farminvite/calendar_list.html", context)


def page_farm_invites_view_hidden_listings(request):
    # all_invites = InviteListing.objects.all().order_by('Invite_Date', 'Invite_Secondary')
    this_moment = datetime.now()
    # only events not past, ordered by date, am then pm.. then secondary listings
    all_invites = InviteListing.objects.filter(
        Q(Show_Listing=False) &
        (Q(Invite_Date=this_moment.date()) |
         Q(Invite_Date__gt=this_moment.date()))).order_by('Invite_Date', 'Invite_Secondary', 'Desired_Time_Slot', )

    context = {
        'contact_good': 'COMPLETE',
        'contact_okay': '85%',
        'contact_poor': '66%',
        'contact_bad': '5%',
        'release': get_version_json(),
        "title": "Farm Range Invites Pending",
        "blurb": "These are pending invites."
        ,
        'all_invites': all_invites,
        "copy_year": datetime.now().year
        # "copy_year": all_loads.prod
    }
    return render(request, "farminvite/calendar_list.html", context)


def page_farm_invites_map(request):
    context = {
        'release': get_version_json(),
        "title": "Farm Invite: Map",
        "table_data": 'Shake it like it\'s going out of style!',
        "copy_year": datetime.now().year
    }
    return render(request, "farminvite/farm_map.html", context)


def page_farm_invites_map_fake(request):
    context = {
        'release': get_version_json(),
        "title": "Coming Soon",
        "blurb": "This page is a place holder for what's to come soon.",
        "table_data": 'Shake it like it\'s going out of style!',
        "copy_year": datetime.now().year
    }
    return render(request, "farminvite/fake_map.html", context)


def page_farm_check_list(request):
    context = {
        'release': get_version_json(),
        "title": "What should I bring?",
        "blurb": "",
        "table_data": 'Strongly recommended items'
                      '<li>Ear protection</li>'
                      '<li>Eye protection</li>'
                      '<li>Chair to sit?</li>'
                      '<li>Shooting mat? Keeps you out of the dirt/mud/snow.</li>'
                      '<li>Firearm (and ammo for said firearm)</li>'
                      '<li>Snacks/Drinks for yourself.</li>'
                      '<li>Sense of humor</li>'
                      '<br />'
                      'Extras if you want...'
                      '<li>Shotgun clays (great rifle targets at 200-600 yards)</li>'
                      '<li>AR500 steel plates, someone\'s bound to damage one eventually</li>'
                      '<li>Donations of brass (i\'ll use it or give it away to someone that can)</li>'
        ,
        "copy_year": datetime.now().year
    }
    return render(request, "farminvite/simple_use_variables.html", context)


def page_request_slot(request):
    context = {
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
                      '<li>My Address: SvenDavison@gmail.com</li>'
                      ''
        ,
        "copy_year": datetime.now().year
    }
    return render(request, "farminvite/simple_use_variables.html", context)


def page_missing_contact_info(request):
    this_moment = datetime.now()
    # only events not past, ordered by date, am then pm.. then secondary listings
    all_invites = InviteListing.objects.filter(
        Q(Invite_Date=this_moment.date()) |
        Q(Invite_Date__gt=this_moment.date())).order_by('Invite_Date', 'Invite_Secondary', 'Desired_Time_Slot', )

    context = {
        # "roll_list": queryset,
        'release': get_version_json(),
        "title": "Missing Contact Info Results In Invite Retraction",
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
    if request.method == 'POST':
        form = InviteListingForm(request.POST)
        if form.is_valid():
            print("VALID")
            form.save()

    context = {
        'release': get_version_json(),
        'form': InviteListingForm(),
        "copy_year": datetime.now().year
    }

    return render(request, 'farminvite/invite_listing_form.html', context)

