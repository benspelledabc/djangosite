from django.db import models
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


class PageCounter(models.Model):
    page_name = models.CharField(max_length=150)
    page_hit_count = models.IntegerField(default=0, null=True)

    def __str__(self):
        return "%s [%s]" % (self.page_name, self.page_hit_count)

    class Meta:
        ordering = ('-page_hit_count', 'page_name')


class PageHideList(models.Model):
    page_name = models.CharField(max_length=150)

    def __str__(self):
        return "%s" % self.page_name

