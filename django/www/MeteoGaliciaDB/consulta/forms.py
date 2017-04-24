from django import forms

class FormRequest(forms.Form):
    lugar = forms.CharField()