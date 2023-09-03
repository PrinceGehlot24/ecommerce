from django.shortcuts import render
from django.views import View
from .models import Customer, Product, OrderPlaced, Cart

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        mobiles = Product.objects.filter(category='M')
        tablets = Product.objects.filter(category='T')
        watches = Product.objects.filter(category='W')
        buds = Product.objects.filter(category='B')
        return render(request,'app/home.html', {'mobiles': mobiles, 'tablets': tablets, 'watches': watches, 'buds': buds })

class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product': product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'Apple' or data == 'Oneplus' or data == 'Samsung' or data == 'Mi':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    return render(request, 'app/mobile.html', { 'mobiles': mobiles })



def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
