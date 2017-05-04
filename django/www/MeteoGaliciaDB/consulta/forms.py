from django import forms
from django.forms import widgets

CHOICES= (
    ('24','24 horas'),
    ('48','48 horas'),
    ('72','72 horas'),
)


opciones_meteosix = (
    ('temperature', 'Temperatura'),
    ('sky_state', 'Estado del cielo'),
    ('precipitation_amount', 'Precipitaciones'),
    ('wind', 'Viento'),
    ('relative_humidity', 'Humedad Relativa'),
    ('cloud_area_fraction', 'Cobertura de nubes'),
    ('snow_level', 'Cota de nieve'),

)

class FormRequest(forms.Form):
    anhos = ('5 años atrás', '10 años atrás', '15 años atrás', '20 años atrás', '25 años atrás', '30 años atrás' \
                 , '40 años atrás','50 años atrás')

    Lugar = forms.CharField()
    Prediccion = forms.ChoiceField(widget=forms.Select, choices=CHOICES)

    Variables = forms.MultipleChoiceField(choices=opciones_meteosix,
                                          widget=widgets.CheckboxSelectMultiple(),
                                          #initial=[variable[0] for variable in opciones_meteosix]
                                          )

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

