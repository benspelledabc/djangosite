from datetime import date
from django.db import models
from enum import Enum


# Create your models here.
class InviteListing(models.Model):
    AM = '8:00am - 11:59am'
    PM = '12:30pm - 4:30pm'
    D1 = '8:00am - 5:00pm'
    N1 = 'NIGHT'
    TIME_SLOT_CHOICES = [
        (AM, '8:00am - 11:59am'),
        (PM, '12:30pm - 4:30pm'),
        (D1, '8:00am - 5:00pm'),
        (N1, 'NIGHT'),
    ]

    Invite_Date = models.DateField(default=date.today)
    Show_Listing = models.BooleanField(default=False)   # False = require approvals
    Desired_Time_Slot = models.CharField(
        max_length=60,
        choices=TIME_SLOT_CHOICES,
        default=AM,
    )

    Invite_Active = 'InviteActive'
    Guest_Canceled_Good = 'GuestCanceledGood'
    Guest_Canceled_Bad = 'GuestCanceledBad'
    Admin_Canceled_Good = 'AdminCanceledGood'
    Admin_Canceled_Bad = 'AdminCanceledBad'
    CANCEL_CODE_CHOICES = [
        (Invite_Active, 'Not Canceled'),
        (Guest_Canceled_Good, 'Guest Canceled, good terms.'),
        (Guest_Canceled_Bad, 'Guest Canceled, bad terms.'),
        (Admin_Canceled_Good, 'Admin Canceled, good terms.'),
        (Admin_Canceled_Bad, 'Admin Canceled, bad terms.'),
    ]
    Cancel_Code = models.CharField(
        max_length=22,
        choices=CANCEL_CODE_CHOICES,
        default=Invite_Active,
    )

    Invite_Secondary = models.BooleanField(default=False, blank=True, null=True)
    Invite_Display_Name = models.CharField(max_length=50, default=None, blank=True, null=True)
    Real_Name = models.CharField(max_length=50, default=None, blank=True, null=True)
    Phone_Number = models.CharField(max_length=20, default=None, blank=True, null=True)
    EMail = models.CharField(max_length=150, default=None, blank=True, null=True)
    Paid = models.BooleanField(default=False, blank=True, null=True)
    Hours_Late = models.DecimalField(max_digits=4, decimal_places=2, default=0.0, null=True)
    Event_Notes = models.TextField(blank=True, null=True)  # i like big comments...

    def __str__(self):
        return "%s %s (Secondary: %s) %s [Show Listing = %s]" % (
            self.Invite_Date,
            self.Invite_Display_Name,
            self.Invite_Secondary,
            self.Phone_Number,
            self.Show_Listing)

    class Meta:
        ordering = ('Invite_Date', 'Invite_Secondary', 'Invite_Display_Name', 'Phone_Number')
