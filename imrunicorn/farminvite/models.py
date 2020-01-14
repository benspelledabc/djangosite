from datetime import date

from django.db import models


# Create your models here.
class InviteListing(models.Model):
    # Manufacture = models.CharField(max_length=150, default=None, blank=True, null=True)
    # Name = models.CharField(max_length=150, default=None, blank=True, null=True)
    # WeightGR = models.DecimalField(max_digits=5, decimal_places=1)
    # Diameter = models.DecimalField(max_digits=5, decimal_places=3)
    # Ballistic_Coefficient = models.DecimalField(max_digits=5, decimal_places=4, default=0.24)
    Invite_Date = models.DateField(default=date.today)
    Invite_AM = models.BooleanField(default=True)
    Invite_PM = models.BooleanField(default=False)
    MDShooters_Name = models.CharField(max_length=50, default=None, blank=True, null=True)
    Phone_Number = models.CharField(max_length=20, default=None, blank=True, null=True)
    EMail = models.CharField(max_length=150, default=None, blank=True, null=True)

    def __str__(self):
        return "%s %s %s" % (self.Invite_Date, self.MDShooters_Name, self.Phone_Number)

    class Meta:
        ordering = ('Invite_Date', 'MDShooters_Name', 'Phone_Number')
