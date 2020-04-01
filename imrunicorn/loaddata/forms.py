from django import forms

from .models import Caliber, Firearm, Powder, Projectile, HandLoad, EstimatedDope


class CaliberForm(forms.ModelForm):
    class Meta:
        model = Caliber
        fields = [
            "name",
            "diameter",
        ]


class PowderForm(forms.ModelForm):
    class Meta:
        model = Powder
        fields = [
            "name",
            "is_smokeless",
        ]
