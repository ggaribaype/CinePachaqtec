from django import forms
from .models import Local

class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = {'nombre', 'direccion', 'tiposervicio', 'precio','distrito','imagen'}