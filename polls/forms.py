from django import forms
from .models import Paste

class PasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = ['content', 'is_public', 'expires_at']
        widgets = {
            'expires_at': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
            }),
        }
