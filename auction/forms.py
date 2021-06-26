from django import forms
from django.forms import ModelForm
from .models import Item, Category, Bid, Comment

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'price', 'image', 'category']
        widgets = { 'price': forms.NumberInput(),
                    'category': forms.Select(choices=Category.objects.all())}

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']