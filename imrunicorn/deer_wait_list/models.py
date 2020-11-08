from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from phone_field import PhoneField


class Recipient(models.Model):
    name = models.CharField(max_length=150)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(blank=True, max_length=254)
    perceived_thankfulness = models.IntegerField(null=True, default=1,
                                                 validators=[
                                                     MaxValueValidator(10),
                                                     MinValueValidator(1)])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class MeatCut(models.Model):
    name = models.CharField(max_length=150)
    level_of_effort = models.IntegerField(null=True, blank=True,
                                          validators=[
                                              MaxValueValidator(10),
                                              MinValueValidator(1)])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Flavor(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class RequestedOrder(models.Model):
    order_date = models.DateField(default=date.today)
    order_complete = models.BooleanField(default=False)
    recipient = models.ForeignKey(Recipient, related_name='recipient', on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    flavor = models.ForeignKey(Flavor, related_name='flavor', on_delete=models.CASCADE, null=True)
    choice_cuts = models.ManyToManyField(MeatCut)

    def __str__(self):
        return "[Order#: %s] [Complete: %s] %s - %s" % (self.pk, self.order_complete, self.order_date, self.recipient)

    class Meta:
        ordering = ('order_complete', '-order_date', '-pk')
 
