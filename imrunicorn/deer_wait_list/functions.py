from django.db.models import Q
from .models import Recipient, MeatCut, Flavor, RequestedOrder


def get_remaining_orders():
    result = RequestedOrder.objects.filter(
        Q(order_complete=False)
    ).order_by('order_date', 'pk')

    return result


def get_all_orders():
    result = RequestedOrder.objects.filter(
    ).order_by('order_date', 'pk')

    return result


def get_all_cuts():
    result = MeatCut.objects.filter(
    ).order_by('name', 'pk')

    return result


def get_all_flavors():
    result = Flavor.objects.filter(
    ).order_by('name', 'pk')

    return result
