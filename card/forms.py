from django import forms
from django.http import request

from .models import Translate

class TransForm(forms.Form):

    title = forms.CharField(max_length=30, label='Перевод:', )

    def __str__(self):
        return self.title
