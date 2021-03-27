from django import forms
from .models import OjasPdfData
class OjasProfileForm(forms.ModelForm):
    class Meta:
        model = OjasPdfData
        fields = ('title','pdf','cover')