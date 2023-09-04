from django.shortcuts import render, redirect
from django.db.models import Q
from django.views import View
from .models import Customer, Product, OrderPlaced, Cart
from .forms import CustomerRegistrationForm, CustomerPorfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

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
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save() 
    return redirect('/cart')

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        totalamount = 0.0
        shippingamount = 70.0
        cart_product = [ p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                temp_amount = (p.quantity * p.product.discounted_price)
                amount += temp_amount
                totalamount = amount + shippingamount
            return render(request, 'app/addtocart.html', {'carts': cart, 'amount': amount, 'totalamount': totalamount})
        else:
            return render(request, 'app/emptycart.html')
        
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [ p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp_amount = (p.quantity * p.product.discounted_price)
            amount += temp_amount
            totalamount = amount + shipping_amount
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)
    
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [ p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp_amount = (p.quantity * p.product.discounted_price)
            amount += temp_amount
            totalamount = amount + shipping_amount
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)

def buy_now(request):
 return render(request, 'app/buynow.html')

def address(request):
 add = Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html', {'add': add, 'active': 'btn-primary'})

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

class ProfileView(View):
    def get(self,request):
        form = CustomerPorfileForm()
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})
    
    def post(self,request):
        form = CustomerPorfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            messages.success(request, 'Congratulations!! Profile Updated Successfully !')
            reg.save()
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})
            
        
