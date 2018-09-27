from django import forms
from .models import Habitacion

class HabForm(forms.ModelForm):
	class Meta:
		model = Habitacion
		fields = ('Codigo_hab','Numero_hab','Precio')