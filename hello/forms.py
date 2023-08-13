from django import forms
from .models import NumberInput

class NumberInputForm(forms.ModelForm):
    class Meta:
        model = NumberInput
        fields = ['number1', 'number2']