from django import forms
from . import models

class FoodItemForm(forms.ModelForm):
    """
    A form for adding a new food item to the database
    """
    
    class Meta:
        model = models.FoodItem
        fields = ['name', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Enter the name of the food item'}),
        }
