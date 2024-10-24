from django import forms
from .models import Cause

class causeForm(forms.ModelForm):
    class Meta:
        model = Cause
        fields = [ 
           'title',
           'details',
           'price_target',
           'price_raised',
           'cause_image'
        ]
