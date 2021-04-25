from datetime import date
from django.db import models
from django.utils.timezone import now


class DockerHubWebhook(models.Model):
    pusher = models.CharField(max_length=450)
    repo_name = models.CharField(max_length=450)
    tag = models.CharField(max_length=450)
    date_created = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return "[%s] %s - %s - %s" % (self.date_created, self.pusher, self.repo_name, self.tag)

    class Meta:
        verbose_name = 'Docker Hub Webhook'
        verbose_name_plural = 'Docker Hub Webhooks'
        ordering = ('-date_created', '-tag')
