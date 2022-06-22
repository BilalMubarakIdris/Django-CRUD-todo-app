from django import forms
from .models import Todoapp


class Todoapp(forms.Model):

    class  Meta:
        model = Todoapp

        fields = [
            'title',
            'description'
        ]