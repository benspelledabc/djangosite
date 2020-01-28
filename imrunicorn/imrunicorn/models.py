# from django.db import models
# from decimal import Decimal
# from datetime import date
# from enum import Enum
#
#
# class SuperCoolInfo(models.Model):
#     Announcement_Date = models.DateField(default=date.today)
#     Announcement_Blurb = models.CharField(max_length=250)
#     Announcement_Body = models.TextField()  # i like big comments...
#
#     def __str__(self):
#         return str(self.Announcement_Date)
#
#     class Meta:
#         ordering = ('Announcement_Date', 'Announcement_Blurb')
