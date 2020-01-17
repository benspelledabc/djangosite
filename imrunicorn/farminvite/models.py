from datetime import date
from django.db import models


# Create your models here.
class InviteListing(models.Model):
    Invite_Date = models.DateField(default=date.today)
    Invite_AM = models.BooleanField(default=True)
    Invite_PM = models.BooleanField(default=False)
    Invite_Secondary = models.BooleanField(default=False, blank=True, null=True)
    MDShooters_Name = models.CharField(max_length=50, default=None, blank=True, null=True)
    Real_Name = models.CharField(max_length=50, default=None, blank=True, null=True)
    Phone_Number = models.CharField(max_length=20, default=None, blank=True, null=True)
    EMail = models.CharField(max_length=150, default=None, blank=True, null=True)
    Hours_Late = models.DecimalField(max_digits=4, decimal_places=2, default=0.0, null=True)
    Event_Notes = models.TextField(blank=True, null=True) # i like big comments...

    def __str__(self):
        return "%s %s (Secondary: %s) %s" % (self.Invite_Date,
                                             self.MDShooters_Name,
                                             self.Invite_Secondary,
                                             self.Phone_Number)

    class Meta:
        ordering = ('Invite_Date', 'Invite_Secondary', 'MDShooters_Name', 'Phone_Number')
