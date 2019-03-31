
# Create your models here.
from django.db import models
from main.models import Product
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Crate(models.Model):
     product=models.ManyToManyField(Product,null=False,related_name="prod")
     buyer=models.OneToOneField(User,unique=True,default=uuid.uuid1,on_delete=models.CASCADE,related_name="cart")