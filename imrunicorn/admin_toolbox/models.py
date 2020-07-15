from datetime import date
from django.db import models
from enum import Enum


# Create your models here.
class RestartRequests(models.Model):
    request_date = models.DateField(default=date.today)
    request_time = models.TimeField(null=True)

    # request_time = models.DateTimeField(auto_now_add=True)
    restart_gunicorn = models.BooleanField(default=True)
    restart_nginx = models.BooleanField(default=True)
    request_cancel = models.BooleanField(default=False)  # False = require approvals

    def __str__(self):
        return "%s @ %s (GUNICORN: %s NGINX: %s)" % (self.request_date,
                            self.request_time,
                            self.restart_gunicorn,
                            self.restart_nginx)

    class Meta:
        ordering = ('-request_date', '-request_time')
        verbose_name = 'Restart Requests'
        verbose_name_plural = 'Restart Requests'
