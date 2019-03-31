from django.db import transaction
from django.shortcuts import render,redirect
from   main.models import Product
from django.contrib.auth.decorators import login_required
from .models import Crate
# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
@login_required(login_url="/login/")
def crated(request, id):
    prod=Product.objects.get(id=id)
    try:
      cra=Crate.objects.get(buyer=request.user)
    except ObjectDoesNotExist:
        with transaction.atomic():
            cra=Crate.objects.create(buyer=request.user)

    cra.product.add(prod)
    return redirect('home')

def cart(request):
    try:
       car=Crate.objects.get(buyer=request.user)
    except ObjectDoesNotExist:
       car=None
    return render(request,'cart/crate.html',{'car':car})
from django.shortcuts import render

# Create your views here.
