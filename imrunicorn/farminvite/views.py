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


# Create your views here.
def unused_json_farm_invites_view(request):
    context = {
        "restart": get_restart_notice,
        'body': 'no body to share',
        'header': 'farm invites view',
    }
    return JsonResponse(context)


def unused_page_farm_invites_view(request):
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
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Farm Invite: Map",
        "table_data": 'Shake it like it\'s going out of style!',
        "copy_year": datetime.now().year
    }
    return render(request, "farminvite/farm_map.html", context)


def page_farm_invites_map_fake(request):
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
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "What should I bring?",
        "blurb": "Pre-pack your car/truck it helps to prevent forgetting things.",
        "table_data": '<ul>'
                      '<strong>Strongly recommended items</strong>'
                      '<li>Ear protection<ul><li>Once mine are in, they don\'t come out for the day.</li></ul></li>'
                      '<li>Eye protection<ul><li>Steel in the eye sucks.</li></ul></li>'
                      '<li>Chair to sit on'
                      '<ul><li>Being prone or standing for 4-8 hours is uncomfortable.</li></ul></li>'
                      '<li>Shooting mat<ul><li>Keeps you out of the dirt/mud/snow and deer poop.</li></ul></li>'
                      '<li>Firearm</li>'
                      '<ul><li>ZEROED (or close) for your ammo.</li><li>AMMO for said firearm.</li></ul>'
                      '<li>Snacks/Drinks for yourself.</li>'
                      '<li>Sense of humor</li>'
                      
                      '<li>Targets (You want to shoot AT something?!)<ul>'
                      '<li>Paper Targets<ul><li>Target Frame to hold targets.'
                      '<ul><li>(Use mine with a $20 deposit.)</li></ul>'
                      '<li>Stapler</li>'
                      '<li>Marker to mark off hits to get the most out of your target.</li></ul>'
                      
                      '<li>AR500 steel plates</li>'
                      '<ul><li>Bring your own or '
                      'shoot my steel after ammo inspection, qualification and additional donation.</li></ul>'
                      '<li>Plastic bottles filled with water (old soda bottles).</li>'
                      '<li>Shotgun clays (great rifle targets at 100-600 yards)</li>'
                      '</ul></li>'
                      '</li></li>'
                      
                      
                      
                      '<br />'
                      '<strong>Extras brownie points</strong>'
                      '<li>Donations of brass (I\'ll use it or give it away to someone that can)</li>'
                      
                      '<br />'
                      '<strong>What to <i>LEAVE AT HOME</i></strong>'
                      '<li>Ego</li>'
                      '</ul>'

        ,
        "copy_year": datetime.now().year
    }
    return render(request, "farminvite/simple_use_variables.html", context)


def page_request_slot(request):
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

