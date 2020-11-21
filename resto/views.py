from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib import messages
from project.models import MenuItem, Feedback
from cart.forms import CartAddProductForm
from resto.forms import ReservationForm, ContactForm
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from utils import send_sms
from webpush import send_group_notification



def home(request):
    feedback = Feedback.objects.order_by('-date')[:3]
    item = MenuItem.objects.all()
    Soepen = MenuItem.objects.filter(category="Soepen")
    Voorgerechten = MenuItem.objects.filter(category="Voorgerechten")
    Momo_gerechten = MenuItem.objects.filter(category="Momo gerechten")
    Noodle_gerechten = MenuItem.objects.filter(category="Noodle gerechten")
    Tandoori_gerechten = MenuItem.objects.filter(category="Tandoori gerechten")
    Kipgerechten = MenuItem.objects.filter(category="Kipgerechten")
    Lamsgerechten = MenuItem.objects.filter(category="Lamsgerechten")
    Zeevruchten_gerechten = MenuItem.objects.filter(category="Zeevruchten gerechten")
    Vegetarische_gerechten = MenuItem.objects.filter(category="Vegetarische gerechten")
    Biryani_gerechten = MenuItem.objects.filter(category="Biryani gerechten")
    Extra = MenuItem.objects.filter(category="Extra's")
    Indiaas_brood = MenuItem.objects.filter(category="Indiaas brood")
    Nagerechten = MenuItem.objects.filter(category="Nagerechten")
    Dranken = MenuItem.objects.filter(category="Dranken")
    return render(request, "index.html",{'item':item,'Soepen':Soepen, 'Voorgerechten': Voorgerechten, 'Momo_gerechten': Momo_gerechten, 'Noodle_gerechten': Noodle_gerechten, 'Tandoori_gerechten': Tandoori_gerechten, 'Kipgerechten': Kipgerechten, 'Lamsgerechten': Lamsgerechten,'Zeevruchten_gerechten': Zeevruchten_gerechten, 'Vegetarische_gerechten': Vegetarische_gerechten, 'Biryani_gerechten': Biryani_gerechten, 'Extra': Extra, 'Indiaas_brood':Indiaas_brood, 'Nagerechten':Nagerechten, 'Dranken':Dranken, 'feedback': feedback,})

def menu1(request):
    item = MenuItem.objects.filter(Menu_type="Home Delivery")
    Soepen = MenuItem.objects.filter(Menu_type="Home Delivery", category="Soepen")
    Voorgerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Voorgerechten")
    Momo_gerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Momo gerechten")
    Noodle_gerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Noodle gerechten")
    Tandoori_gerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Tandoori gerechten")
    Kipgerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Kipgerechten")
    Lamsgerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Lamsgerechten")
    Zeevruchten_gerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Zeevruchten gerechten")
    Vegetarische_gerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Vegetarische gerechten")
    Biryani_gerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Biryani gerechten")
    Extra = MenuItem.objects.filter(Menu_type="Home Delivery", category="Extra's")
    Indiaas_brood = MenuItem.objects.filter(Menu_type="Home Delivery", category="Indiaas brood")
    Nagerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Nagerechten")
    Dranken = MenuItem.objects.filter(Menu_type="Home Delivery", category="Dranken")
    cart_product_form = CartAddProductForm()
    return render(request, "menu1.html",
                  {'item': item, 'Soepen':Soepen, 'Voorgerechten': Voorgerechten, 'Momo_gerechten': Momo_gerechten, 'Noodle_gerechten': Noodle_gerechten, 'Tandoori_gerechten': Tandoori_gerechten, 'Kipgerechten': Kipgerechten, 'Lamsgerechten': Lamsgerechten,

                   'Zeevruchten_gerechten': Zeevruchten_gerechten, 'Vegetarische_gerechten':Vegetarische_gerechten, 'Biryani_gerechten': Biryani_gerechten, 'Extra': Extra, 'Indiaas_brood':Indiaas_brood, 'Nagerechten':Nagerechten, 'Dranken':Dranken, 'cart_product_form':cart_product_form })

def menu3(request):
    item = MenuItem.objects.filter(Menu_type="Takeaway")
    Soepen = MenuItem.objects.filter(Menu_type="Takeaway", category="Soepen")
    Nepali_menu = MenuItem.objects.filter(Menu_type="Takeaway", category="Nepali Menu")
    Voorgerechten = MenuItem.objects.filter(Menu_type="Takeaway", category="Voorgerechten")
    Momo_gerechten = MenuItem.objects.filter(Menu_type="Takeaway", category="Momo gerechten")
    Noodle_gerechten = MenuItem.objects.filter(Menu_type="Takeaway", category="Noodle gerechten")
    Tandoori_gerechten = MenuItem.objects.filter(Menu_type="Takeaway", category="Tandoori gerechten")
    Kipgerechten = MenuItem.objects.filter(Menu_type="Takeaway", category="Kipgerechten")
    Lamsgerechten = MenuItem.objects.filter(Menu_type="Takeaway", category="Lamsgerechten")
    Zeevruchten_gerechten = MenuItem.objects.filter(Menu_type="Takeaway", category="Zeevruchten gerechten")
    Vegetarische_gerechten = MenuItem.objects.filter(Menu_type="Takeaway", category="Vegetarische gerechten")
    Biryani_gerechten = MenuItem.objects.filter(Menu_type="Takeaway", category="Biryani gerechten")
    Extra = MenuItem.objects.filter(Menu_type="Takeaway", category="Extra's")
    Indiaas_brood = MenuItem.objects.filter(Menu_type="Takeaway", category="Indiaas brood")
    Nagerechten = MenuItem.objects.filter(Menu_type="Takeaway", category="Nagerechten")
    Dranken = MenuItem.objects.filter(Menu_type="Takeaway", category="Dranken")
    cart_product_form = CartAddProductForm()
    return render(request, "menu3.html",
                  {'item': item, 'Soepen':Soepen, 'Voorgerechten': Voorgerechten, 'Momo_gerechten': Momo_gerechten, 'Noodle_gerechten': Noodle_gerechten, 'Tandoori_gerechten': Tandoori_gerechten, 'Kipgerechten': Kipgerechten, 'Lamsgerechten': Lamsgerechten, 'Nepali_menu': Nepali_menu,

                   'Zeevruchten_gerechten': Zeevruchten_gerechten, 'Vegetarische_gerechten':Vegetarische_gerechten, 'Biryani_gerechten': Biryani_gerechten, 'Extra': Extra, 'Indiaas_brood':Indiaas_brood, 'Nagerechten':Nagerechten, 'Dranken':Dranken, 'cart_product_form':cart_product_form })

def menu2(request):
    item = MenuItem.objects.filter(Menu_type="Home Delivery")
    Soepen = MenuItem.objects.filter(Menu_type="Home Delivery", category="Soepen")
    Voorgerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Voorgerechten")
    Momo_gerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Momo gerechten")
    Noodle_gerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Noodle gerechten")
    Tandoori_gerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Tandoori gerechten")
    Kipgerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Kipgerechten")
    Lamsgerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Lamsgerechten")
    Zeevruchten_gerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Zeevruchten gerechten")
    Vegetarische_gerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Vegetarische gerechten")
    Biryani_gerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Biryani gerechten")
    Extra = MenuItem.objects.filter(Menu_type="Home Delivery", category="Extra's")
    Indiaas_brood = MenuItem.objects.filter(Menu_type="Home Delivery", category="Indiaas brood")
    Nagerechten = MenuItem.objects.filter(Menu_type="Home Delivery", category="Nagerechten")
    Dranken = MenuItem.objects.filter(Menu_type="Home Delivery", category="Dranken")
    cart_product_form = CartAddProductForm()
    return render(request, "menu2.html",
                  {'item': item, 'Soepen':Soepen, 'Voorgerechten': Voorgerechten, 'Momo_gerechten': Momo_gerechten, 'Noodle_gerechten': Noodle_gerechten, 'Tandoori_gerechten': Tandoori_gerechten, 'Kipgerechten': Kipgerechten, 'Lamsgerechten': Lamsgerechten,

                   'Zeevruchten_gerechten': Zeevruchten_gerechten, 'Vegetarische_gerechten':Vegetarische_gerechten, 'Biryani_gerechten': Biryani_gerechten, 'Extra': Extra, 'Indiaas_brood':Indiaas_brood, 'Nagerechten':Nagerechten, 'Dranken':Dranken, 'cart_product_form':cart_product_form })

class NewReservation(CreateView):
    template_name = "reservation.html"
    form_class = ReservationForm

    @csrf_exempt
    def form_valid(self, form):
        name = form.cleaned_data['first_name']
        people = form.cleaned_data['people']
        time = form.cleaned_data['time']
        date = form.cleaned_data['date_reserved']
        new = form.save(commit=False)
        new.save()
        # sends a flash message to the user
        messages.success(
            self.request,
            "you have successfully booked a new" +
            " table confirm your by paying for the table ")
        # redirect the user back to his/her dashboard
        user = self.request.user
        return redirect("/thanks")


class Contact(CreateView):
    template_name = "contact.html"
    form_class = ContactForm

    def form_valid(self, form):
        new = form.save(commit=False)
        new.save()
        # send a flash message to the user
        messages.success(
            self.request,
            "your message was sent successfully")
        # redirect the user back to contact page
        return redirect("/contact")


@csrf_exempt
def thankyou(request):
    return render(request, 'payment_done.html')


@csrf_exempt
def thanks(request):
    return render(request, 'thankyou.html')

@csrf_exempt
def sorry(request):
    return render(request, 'sorry.html')

@csrf_exempt
def soon(request):
    return render(request, 'soon.html')


def payment(request):
    return render(request, "payment.html")
