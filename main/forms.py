from django import forms

class PreprocessingForm(forms.Form):
    name = forms.CharField(label = 'Your name', max_length = 100)
    message = forms.CharField(max_length = 600, widget = forms.Textarea)