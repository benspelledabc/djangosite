from django.db import models

# Create your models here.


class WatchItem(models.Model):
    item_name = models.CharField(max_length=150, default=None, blank=True, null=True)
    item_phrase = models.CharField(max_length=250, default=None, blank=True, null=True)
    item_link = models.TextField(blank=True, null=True)  # i like big comments...
    item_phrase_not_exist = models.BooleanField(default=False, blank=True, null=True)
    item_exception = models.CharField(max_length=250, default=None, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.item_name, self.item_phrase)

    class Meta:
        ordering = ('item_name', 'item_phrase')

