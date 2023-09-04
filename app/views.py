from django.shortcuts import render
from django.db.models import Q
from django.views import View
from .models import Customer, Product, OrderPlaced, Cart
from .forms import CustomerRegistrationForm
from django.contrib import messages

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

def mobile(request, data=None, sort=None):
    filter_dict = {
        None: Q(category='M'),
        'newarrivals': Q(),
        'lowtohigh': Q(),
        'hightolow': Q(),
        'above50000': Q(discounted_price__gt=50000),
        'below50000': Q(discounted_price__lt=50000),
        'below30000': Q(discounted_price__lt=30000),
        'below15000': Q(discounted_price__lt=15000),
    }
    
    brand_filter = Q()
    if data in ['Apple', 'Oneplus', 'Samsung', 'Mi']:
        brand_filter = Q(brand=data)
    
    filter_combination = filter_dict.get(sort, Q())
    mobiles = Product.objects.filter(Q(category='M') & brand_filter & filter_combination)
    
    return render(request, 'app/mobile.html', {'mobiles': mobiles, 'data': data})


def login(request):
 return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
  def get(self, request):
    form = CustomerRegistrationForm()
    return render(request, 'app/customerregistration.html', {'form': form })
    
  def post(self, request):
    form = CustomerRegistrationForm(request.POST)
    if form.is_valid():
        messages.success(request, 'Congratulations !! Registered Successfully .')
        form.save()
    return render(request, 'app/customerregistration.html', {'form': form})
        



def checkout(request):
 return render(request, 'app/checkout.html')
