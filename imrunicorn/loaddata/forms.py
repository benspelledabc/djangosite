from django import forms

from .models import Caliber, Firearm, Powder, Projectile, HandLoad, EstimatedDope


class CaliberForm(forms.ModelForm):
    # author_pk = forms.IntegerField(widget=forms.IntegerField(attrs={"readonly": "readonly"}))

    class Meta:
        model = Caliber
        fields = [
            "name",
            "diameter",
        ]


# class RawCaliberForm(forms.Form):
#     author_pk = forms.IntegerField(readonly="True")
