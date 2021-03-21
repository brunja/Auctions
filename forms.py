from django import forms
from django.forms import ModelForm
from .models import Item, Category

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'price', 'image', 'category']
        widgets = { 'price': forms.NumberInput(),
                    'category': forms.Select(choices=Category.objects.all())}