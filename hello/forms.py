from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import EasterInput
from .models import JulianInput

class EasterInputForm(forms.ModelForm):
    class Meta:
        model = EasterInput
        fields = ['year']
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['year'].validators.append(MinValueValidator(1583))

class JulianInputForm(forms.ModelForm):
    class Meta:
        model = JulianInput
        fields = ['year','month', 'day', 'hour', 'minute', 'seconds']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['year'].validators.append(MinValueValidator(-4712))
        self.fields['month'].validators.append(MinValueValidator(1))
        self.fields['month'].validators.append(MaxValueValidator(12))
        self.fields['day'].validators.append(MinValueValidator(1))
        self.fields['day'].validators.append(MaxValueValidator(31))
        self.fields['hour'].validators.append(MinValueValidator(0))
        self.fields['hour'].validators.append(MaxValueValidator(23))
        self.fields['minute'].validators.append(MinValueValidator(0))
        self.fields['minute'].validators.append(MaxValueValidator(59))
        self.fields['seconds'].validators.append(MinValueValidator(0))
        self.fields['seconds'].validators.append(MaxValueValidator(60))
