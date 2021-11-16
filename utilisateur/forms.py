from django import forms


class User_form(forms.Form):
    nom = forms.CharField(min_length=2)
    prenom = forms.CharField(min_length=3)
