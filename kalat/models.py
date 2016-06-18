from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime


class kalat(models.Model):
	paikka = models.CharField(max_length = 30)
	saaja = models.CharField(max_length = 300)
	viehe = models.CharField(max_length = 300)
	paino = models.CharField(max_length = 10)
	pituus = models.CharField(max_length = 10 )
	#saantipäivä = models.DateTimeField('date published')
	kuva = models.ImageField(upload_to="images", default = "images/default.jpg")
	public = models.BooleanField()
	def __str__(self): 
		return "Saaja: " + self.saaja+ " Paikka: " + self.paikka + " Viehe: " + self.viehe + " Paino:" + self.paino + " Pituus: " + self.pituus
# Create your models here.
