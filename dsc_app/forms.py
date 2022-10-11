from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title','description','image','slug')
        widgets = {'url': forms.HiddenInput,}


