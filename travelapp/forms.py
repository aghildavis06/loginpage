from django import forms
from .models import crud
class items_form(forms.ModelForm):
    class Meta:
        model=crud
        fields=['name','description']
        