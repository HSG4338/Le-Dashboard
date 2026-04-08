from django import forms
from .models import Suggestion


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['name', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name (optional)', 'class': 'glass-input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Share a thought...', 'class': 'glass-input', 'rows': 5}),
        }

    def clean_message(self):
        msg = self.cleaned_data.get('message', '').strip()
        if len(msg) < 10:
            raise forms.ValidationError("Please write at least 10 characters.")
        return msg
