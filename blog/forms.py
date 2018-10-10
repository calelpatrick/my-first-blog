from django import forms
from .models import Habitacion
from .models import Post

class HabForm(forms.ModelForm):
	class Meta:
		model = Habitacion
		fields = ('Codigo_hab','Numero_hab','Precio')

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','text',)
