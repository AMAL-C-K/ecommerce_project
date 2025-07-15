from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from cart_app.models import Cart, Checkout
from ecom_app.models import Products
from django.core.exceptions import ObjectDoesNotExist
import razorpay
from django.views.decorators.csrf import csrf_exempt



@login_required(login_url='signin')
def add_to_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    cart_item = Cart.objects.create(product=product, quantity=1, user=request.user)
    cart_item.save()
    return redirect('view_cart')



@login_required(login_url='signin')
def view_cart(request, cart=None, subtotal=0, count=0):
    try:
        cart = Cart.objects.filter(user=request.user,ordered=False).order_by('-created_at')
    except ObjectDoesNotExist:
        pass
        
    context = {
        'cart': cart,
        'subtotal': subtotal,
        'count': count,

    }

    return render(request, 'cart.html', context)

@login_required(login_url='signin')
def dec_quantity(request, cart_id):
    # product = get_object_or_404(Products, id=product_id)
    cart = Cart.objects.get(id=cart_id)
    if cart.quantity > 1:
        cart.quantity -= 1
        cart.save()
    else:
        cart.delete()
    return redirect('view_cart')


@login_required(login_url='signin')
def add_quantity(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    if cart.quantity >= 1:
        cart.quantity += 1
        cart.save()

    return redirect('view_cart')


@login_required(login_url='signin')
def delete(request, cart_id):
    cart= Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect('view_cart')


@login_required(login_url='signin')
def checkout(request, cart_id):
    payment = ""
    cart = Cart.objects.get(id=cart_id)
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        amount = int(request.POST.get('amount')) * 100
        client = razorpay.Client(auth=('rzp_test_j3CDH5AT9kIHCA', 'G4gthDwLFYppB5jpJvNsqpj2'))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        print(payment)
        payments = Checkout.objects.create(cart=cart, amount=amount, payment_id=payment['id'],
                                           product_name=product_name)
        payments.save()

    return render(request, 'checkout.html', {'cart': cart, 'payment': payment})



@csrf_exempt
def success(request):
    if request.method == 'POST':
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        order = Checkout.objects.filter(payment_id=order_id).first()
        order.paid = True
        order.save()
        
        cart = Cart.objects.get(id=order.cart.id)   
        if order.paid == True: 
            cart.ordered = True
            cart.save()
            
        print(cart.ordered)
        print(a)
    return render(request, 'success.html')


@login_required(login_url='signin')
def orders(request):
    orders = Checkout.objects.filter(cart__user=request.user, paid=True).order_by('-id')
    return render(request, 'orders.html',{'orders':orders})

