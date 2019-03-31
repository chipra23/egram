from django.urls import path
from . import views
from cart import views as cart_view

urlpatterns=[
path('add/',views.addproduct,name='add'),
path('it/',views.myproduct,name='list'),
path('',views.account,name='acc'),
path('<id>/',views.productdetail,name='detail'),
path('cart',cart_view.cart,name='cart'),
path('crat/<id>',cart_view.crated,name='crat')
]
