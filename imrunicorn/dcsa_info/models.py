from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from phone_field import PhoneField


class RequestTimeline(models.Model):
    EMAIL = 'Email'
    SNAIL_MAIL = 'Snail Mail'
    OTHER = 'Other'

    submission_format_choices = [
        (EMAIL, 'Email'),
        (SNAIL_MAIL, 'Snail Mail'),
        (OTHER, 'Other'),
    ]

    submission_format = models.CharField(
        max_length=20,
        choices=submission_format_choices,
        default=EMAIL,
    )

    request_date = models.DateField(default=date.today)
    requester_alias = models.CharField(max_length=50, null=False)
    ticket_number_received = models.DateField(null=True, blank=True)
    ticket_number = models.CharField(max_length=150, null=True, blank=True)
    result_date = models.DateField(null=True, blank=True)
    received_pa_info_requested = models.BooleanField(default=False)
    request_text = models.TextField(blank=True, null=True)  # i like big comments...

    def __str__(self):
        return "[%s] %s - %s" % (self.pk, self.request_date, self.requester_alias)

    class Meta:
        ordering = ('-request_date', '-pk', 'requester_alias')
        permissions = [
            ("ticket_number_viewer", "Can view ticket numbers"),
        ]


