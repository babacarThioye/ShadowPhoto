from django import forms
from django.forms import NumberInput


class Photo_form(forms.Form):
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), required=True)
    heure = forms.TimeField(widget=NumberInput(attrs={'type': 'time'}), required=True)


class Photo_form_Add(Photo_form):
    image = forms.ImageField(required=True)
