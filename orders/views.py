from django.shortcuts import render, get_object_or_404, redirect
from .models import OrderItem, Order
from .forms import OrderCreateForm, OrderUpdateForm
from django.urls import reverse
from decimal import *
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from paypal.standard.forms import PayPalPaymentsForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cart.cart import Cart
from django.conf import settings
from project.models import Reservation
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from utils import send_sms
from webpush import send_group_notification

import stripe

def order_create(request, **kwargs):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    menuitem=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                    time = datetime.now()
                )

        return render(request, 'orders/order/created.html', {'order': order, 'cart': cart })
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})


def charge(request,  product_id, **kwargs):
    pd_key = product_id
    items = OrderItem.objects.filter(order=product_id)
    fix =0 
    for i in items:
      fix += Decimal(i.quantity)*Decimal(i.price)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    pub_key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        customer = stripe.Customer.create( source=request.POST['stripeToken'])
        charge = stripe.Charge.create(customer =customer.id, amount = int(fix*100), currency = 'eur',description = "product_id"+str(product_id))
        return redirect('orders:email_one', product_id=product_id)  
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': fix,
        'item_name': "product_id"+str(product_id)+"-diwali palace",
        'invoice': str(product_id),
        'currency_code': 'EUR',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('orders:email_one', args=[product_id])),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('orders:payment_cancelled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    cost = (fix*100)
    amountcost = int(fix*100)
    return render(request, 'orders/payments/pay.html', {'items': items, 'pub_key': pub_key, 'cost': cost, 'pd_key': pd_key, 'form': form, 'fix': fix, 'product_id': product_id,'amountcost':amountcost})
    return HttpResponseRedirect('/')

 
 
@csrf_exempt
def payment_canceled(request):
    return render(request, 'orders/payments/payment_cancelled.html') 


class UpdateOrder(LoginRequiredMixin, UpdateView):
    """Admin user updates all the reservation."""
    form_class = OrderUpdateForm
    template_name = "orders/updates/update_order.html"
    model = OrderItem

    def get_object(self, *args, **kwargs):
        obj = get_object_or_404(OrderItem, pk=self.kwargs['pk'])
        return obj

    def form_valid(self, form, **kwargs):
        val = form.cleaned_data['status']
        form.save()
        messages.success(
            self.request, "you have successfully updated the reservation")
        if val == "Complete":
            return redirect('orders:email_two', pk=self.kwargs['pk'])
        if val == "confirmed":
            return redirect('orders:email_status', pk=self.kwargs['pk'])
        return redirect('/dashboard')

def email_one(request, product_id):
    #sending billing email
    subject = "Your Order From Diwali Palace"
    from_email = settings.EMAIL_HOST_USER
    order = OrderItem.objects.filter(order_id=product_id).first()
    to = [order.order.email]
    items = OrderItem.objects.filter(order_id=product_id)
    price = 0
    for i in items:
        price += Decimal(i.price)*Decimal(i.quantity)
    ctx = {
        'order': order,
        'items': items,
        'price':price,
    }

    message = get_template('orders/order/email-1.html').render(ctx)
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()
    #clearing cart
    cart = Cart(request)
    cart.clear()
    #confirming payment status sucessful in database
    xo = Order.objects.filter(id=product_id).update(paid=1)
    yo = OrderItem.objects.filter(order_id=product_id).update(status='pending')
    #sending push notification to staff    
    return HttpResponseRedirect('/thankyou')



def email_five(request, product_id):
    #sending billing email
    subject = "Your Order From Diwali Palace"
    from_email = settings.EMAIL_HOST_USER
    order = OrderItem.objects.filter(order_id=product_id).first()
    to = [order.order.email]
    items = OrderItem.objects.filter(order_id=product_id)
    price = 0
    for i in items:
        price += Decimal(i.price)*Decimal(i.quantity)
    ctx = {
        'order': order,
        'items': items,
        'price':price,
    }

    message = get_template('orders/order/email-1.html').render(ctx)
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()
    #clearing cart
    cart = Cart(request)
    cart.clear()
    #confirming payment status sucessful in database
    yo = OrderItem.objects.filter(order_id=product_id).update(status='pending')
    #sending push notification to staff
    
    return HttpResponseRedirect('/thankyou')

def email_two(request, pk):
    subject = "What do you think of your order at Diwali Palace ?, Rate Us  !! 👍🍽👎"
    from_email = settings.EMAIL_HOST_USER
    order = OrderItem.objects.filter(pk=pk).first()
    fix_url = HttpResponseRedirect('/add-feedback')
    to = [order.order.email]
    ctx = {
        'order': order,
        'fix_url':fix_url,
    }

    message = get_template('orders/order/feedback.html').render(ctx)
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()
    return HttpResponseRedirect('/dashboard')

def email_status(request, pk):
    subject = "Your order at Diwali Palace , confirmed  !! 👍🍽👎"
    from_email = settings.EMAIL_HOST_USER
    order = OrderItem.objects.filter(pk=pk).first()
    to = [order.order.email]
    ctx = {
        'order': order,
    }

    message = get_template('orders/order/confirmation_email.html').render(ctx)
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()
    return HttpResponseRedirect('/dashboard')

def reservation_status(request, pk):
    subject = "Your Reservation at Diwali Palace , confirmed  !! 👍🍽👎"
    from_email = settings.EMAIL_HOST_USER
    reservation = Reservation.objects.filter(pk=pk).first()
    to = [reservation.email]
    ctx = {
        'reservation': reservation,
    }

    message = get_template('orders/order/reservation_email.html').render(ctx)
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()
    return HttpResponseRedirect('/dashboard')



def ideal(request, product_id, amountcost):
    return render(request, 'orders/payments/ideal.html',{'product_id': product_id,'cost': amountcost})


def authback(request, product_id, amountcost):
    su = request.GET.get('source', '')
    stripe.api_key = settings.STRIPE_SECRET_KEY
    charge = stripe.Charge.create(
        amount=amountcost,
        currency='eur',
        source=su,
    )
    return redirect('orders:email_one', product_id=product_id)
