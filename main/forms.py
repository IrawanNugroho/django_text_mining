from django import forms

class PreprocessingForm(forms.Form):
    message = forms.CharField(widget = forms.Textarea)