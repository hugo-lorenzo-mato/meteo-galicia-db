from django import forms


class FormRequest(forms.Form):
    anhos = ('5 años atrás', '10 años atrás', '15 años atrás', '20 años atrás', '25 años atrás', '30 años atrás' \
                 , '40 años atrás','50 años atrás')

    lugar = forms.CharField()

    a = forms.Form()
    '''
    seleccione_mes_dia_y_años_atrás = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Seleccione año", "Seleccione mes", "Seleccione día"), years=anhos))
    e = forms.CheckboxInput



   b = forms.DateTimeField
   d = forms.BooleanField
   e = forms.CheckboxInput
   d = forms.ComboField
   e = forms.DateTimeInput
   f = forms.DateInput
   #g = forms.ModelMultiplChoiceField
   h = forms.TypedMultipleChoiceField
   i = forms.TimeInput
   j = forms.Widget
   k = forms.SplitDateTimeWidget
   l = forms.SplitDateTimeField
   m = forms.SelectDateWidget
   #n = forms.ModelChoiceField()
'''

