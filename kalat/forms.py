from django import forms
from .models import kalat

class SaalisForm(forms.ModelForm):
	class Meta:
		model = kalat
		fields = [
		"paikka",
		"saaja",
		"viehe",
		"paino",
		"pituus",
		"kuva",
		"public",
		]
"""
class NameForm(forms.Form):
    saaja = forms.CharField(label='Your name', max_length=100)
    paikka = forms.CharField(label = 'Paikka', max_length = 30)
    viehe = forms.CharField(label = 'Viehe', max_length = 300)
    paino = forms.CharField(label = 'Paino', max_length = 10)
    pituus = forms.CharField(label = 'Pituus', max_length = 10)
	kuva = models.ImageField(upload_to="images", default = "images/default.jpg")
	
"""