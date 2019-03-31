from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
	image = models.ImageField()
	product= models.CharField(max_length=150)
	description = models.TextField()
	rate = models.CharField(max_length=150)
	date = models.DateTimeField(auto_now_add=True)
	Quantity = models.CharField(max_length=30)
	seller = models.ForeignKey(User,default=None,on_delete=models.CASCADE,null=False,related_name='userrel')

	def snippet(self):
		return self.description[:50]+'...'
