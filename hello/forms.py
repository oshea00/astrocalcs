from django import forms
from django.core.validators import MinValueValidator
from .models import EasterInput

class EasterInputForm(forms.ModelForm):
    class Meta:
        model = EasterInput
        fields = ['year']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['year'].validators.append(MinValueValidator(1583))
