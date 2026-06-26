from django import forms
from datetime import date

class food_form(forms.Form):
    name = forms.CharField(
        max_length = 30,
        label = 'Name of food',
        required=False,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name of food',
        })
    )
    calories = forms.IntegerField(
        min_value = 0,
        max_value = 1e6,
        required=True,
        widget = forms.HiddenInput()
    )
    unit_calories = forms.IntegerField(
        min_value = 1,
        max_value = 1e4,
        label = 'Unit calories (kCal/unit)',
        required=True,
        widget = forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Unit calories (in nutrition facts)',
        })
    )
    quantity = forms.IntegerField(
        min_value = 1,
        initial = 1,
        label = 'Quantity of units of food',
        required=True,
        widget = forms.NumberInput(attrs={
            'class': 'form-control',
            'value': '1',
        })
    )

class water_form(forms.Form):
    amount = forms.IntegerField(
        min_value = 0,
        max_value = 1e4,
        label = 'Volume of water (mL)',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Amount',
        })
    )