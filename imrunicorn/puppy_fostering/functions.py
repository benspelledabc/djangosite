import json
import datetime
# from datetime import datetime
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Momma, Puppy, PuppyNotes, MommaPhoto
from django.db.models import Q, Count
from django.db.models.functions import TruncHour, TruncMonth, TruncYear
from django.db.models.functions import ExtractMonth
from django.contrib.auth.models import User


def puppies_by_sex(sex="Both"):
    if sex == "Both":
        result = Puppy.objects.all()
    else:
        result = Puppy.objects.filter(
            Q(sex=sex)
        )
    return result


def puppies_by_momma(momma="All"):
    if momma == "All":
        result = Puppy.objects.all()
    else:
        result = Puppy.objects.filter(
            Q(momma=momma)
        )
    return result
