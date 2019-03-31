from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def mainf(request):
	products=Product.objects.all()
	return render(request,'main/home.html',{'products':products})

@login_required(login_url="/login/")
def account(request):
	return render(request,'main/account.htm',{})

@login_required(login_url="/login/")
def addproduct(request):
	if request.method=='POST':
		form=forms.AddProduct(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.seller = request.user
			instance.save()

			return redirect('home')
	else:
		form=forms.AddProduct()
	return render(request,'main/addproduct.html',{'form':form})


def myproduct(request):
		current_user=request.user
		print(current_user.id)
		productor=Product.objects.filter(seller=current_user)
		#productor = get_object_or_404(Product,seller=current_user)
		return render(request,'main/myproducts.html',{'productor':productor})


def productdetail(request,id):
	try:
		productdet=get_object_or_404(Product,id=id)
		return render(request,'main/product_detail.html',{'productdet':productdet})
	except ValueError:
		return redirect('home')


