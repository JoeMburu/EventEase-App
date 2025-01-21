from django import forms
from .models import Event
from crispy_forms.layout import Layout, Div, Submit
from crispy_forms.helper import FormHelper

class EventRegisterForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location', 'category', 'tags', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3 form-control-lg', 'type':'text'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control mb-3',  # Add Bootstrap styling
                'rows': 6,  # Adjust the height of the Textarea
                'placeholder': 'Enter a detailed description of the event',               
            }),
             'date': forms.DateInput(attrs={'class': 'form-control mb-3 form-control-lg', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control mb-3 form-control-lg', 'type': 'time'}),
            'location': forms.TextInput(attrs={'class': 'form-control-lg', 'placeholder': 'Event Location'}),
            'category': forms.TextInput(attrs={'class': 'form-control-lg'}),
            'tags': forms.TextInput(attrs={'class': 'form-control-lg'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-lg'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div('title', css_class='mb-3'),
            Div('description', css_class='mb-3'),
            Div('date', css_class='mb-3'),
            Div('time', css_class='mb-3'),
            Div('location', css_class='mb-3'),
            Div('category', css_class='mb-3'),
            Div('tags', css_class='mb-3'),
            Div('image', css_class='mb-3'),
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )    