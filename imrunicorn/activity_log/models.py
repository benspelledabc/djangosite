from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Activity(models.Model):
    name = models.CharField(max_length=150, default=None, blank=True, null=True)
    description = models.TextField(blank=True, null=True)  # i like big comments...
    sfw = models.BooleanField(default=False)
    transaction_amount = models.IntegerField(
        null=True,
        default=-2,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(-100)
        ]
     )

    def __str__(self):
        return "[cost: %s] %s" % (self.transaction_amount, self.name)

    class Meta:
        ordering = ('-transaction_amount', 'name')
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'


class ActivityLog(models.Model):
    actor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=date.today)
    time = models.TimeField(null=True)
    actor_comments = models.TextField(blank=True, null=True)  # i like big comments...

    def __str__(self):
        return "[%s %s] %s - %s" % (self.date, self.time, self.actor, self.activity.name)

    class Meta:
        ordering = ('-date', '-time')
        verbose_name = 'Activity Log'
        verbose_name_plural = 'Activity Logs'


class ActivityPhotoValidation(models.Model):
    activity_log = models.ForeignKey(ActivityLog, on_delete=models.CASCADE, null=True)
    caption = models.CharField(max_length=350, default=None, blank=True, null=True)
    photo_proof = models.ImageField(upload_to='uploads/activity_log/', null=True, blank=True)

    def __str__(self):
        return "%s" % self.activity_log

    class Meta:
        ordering = ('-activity_log', 'id')
        verbose_name = 'Activity Photo Validation'
        verbose_name_plural = 'Activity Photo Validations'
