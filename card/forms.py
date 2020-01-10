from django import forms
from .models import Cards
from django.http import request


class TransForm(forms.Form):

    title = forms.CharField(max_length=30, label='Перевод:', )

    def __str__(self):
        return self.title


class CardForm(forms.ModelForm):

    class Meta:
        model = Cards
        fields = ('category', 'slug', 'text', 'translate', 'user', )
