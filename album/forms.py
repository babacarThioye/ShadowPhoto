from django import forms


class Album_form(forms.Form):
    titre = forms.CharField(required=True, help_text="Titre de l\'album")
    public = forms.BooleanField(initial=True, required=False)
