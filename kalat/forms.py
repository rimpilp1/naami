from django import forms
from .models import kalat
import datetime
from django.conf import settings

class SaalisForm(forms.ModelForm):
	#"saantipaiva" = forms.DateField(widget=SelectDateWidget(), initial=yesterday)
	
	class Meta:
		model = kalat
		fields = [
        "saaja",
		"paikka",
		"paino",
		"pituus",
        "viehe",
		"email",
        "saantipaiva",
		"kuva",
		"public",
		]
		labels = {
			"email": "Sähköposti",
		}
		widgets = {
			'saantipaiva': forms.SelectDateWidget(),
		}

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20)