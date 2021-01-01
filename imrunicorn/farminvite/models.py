from datetime import date
from django.db import models
from enum import Enum
from django.core.validators import MaxValueValidator, MinValueValidator


class PackingListItem(models.Model):
    Name = models.CharField(max_length=150)
    # Count = models.IntegerField(null=True, default=1, validators=[MaxValueValidator(9000), MinValueValidator(1)])

    def __str__(self):
        return '%s' % self.Name

    class Meta:
        ordering = ('Name',)


class PackingList(models.Model):
    Items = models.ManyToManyField(PackingListItem)
    List_Date = models.DateField(default=date.today)

    def __str__(self):
        return '%s' % self.List_Date

    class Meta:
        ordering = ('-List_Date',)


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
        # return "%s %s (Paid: %s) [Show Listing = %s] [ID: %s]" % (
        return '{"Invite_Date": "%s", "Paid": %s, "id": %s, "Show_Listing": %s, "Invite_Display_Name": "%s"}' % (
            self.Invite_Date,
            str(self.Paid).lower(),
            self.id,
            str(self.Show_Listing).lower(),
            self.Invite_Display_Name
        )

    class Meta:
        ordering = ('-Paid', 'id', 'Invite_Date')
