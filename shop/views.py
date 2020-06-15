from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from . models import *
# Create your views here.
def index(request):
    products = Product.objects.all()
    params = {'Product' : products}
    return render(request, 'shop/index.html',params)


def shop(request):
    products = Product.objects.all()
    params = {'Product' : products}
    return render(request, 'shop/shop.html', params)



def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')



def about(request):
    return render(request, 'shop/about.html')
def search(request):
    return HttpResponse("ye search hai")




def tracker(request):
    return HttpResponse("ye tracker hai")



def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, ordered = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        order = {'get_cart_total':0, 'get_cart_items':0}
        items = []
    params = {'items':items, 'order':order}
    return render(request, 'shop/checkout.html', params)




def Cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        item = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    params = {'items':items, 'order':order}
    return render(request, 'shop/cart.html',params)




def productView(request, id):
    #fetch the product using id
    product = Product.objects.filter(id=id)
    params = {'product':product[0]}
    return render(request, 'shop/productview.html', params)
    



