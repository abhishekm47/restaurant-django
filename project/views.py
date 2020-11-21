from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import View, CreateView
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView
from project.forms import UpdateUser, ReservationForm, LoginForm, RegisterForm, MenuForm, FeedbackForm, ReservationUpdateForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from decimal import *
from django.http import JsonResponse
from project.models import User, Reservation, MenuItem
from orders.models import OrderItem
from django.template import RequestContext, Template
from django.template.loader import render_to_string, get_template 


class Profile(LoginRequiredMixin, UpdateView):
    """admin user view and update profile"""
    form_class = UpdateUser
    model = User
    template_name = "super/profile.html"
    login_url = "/login/"

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, ("your profile has been updated successfully"))
        return redirect('/profile')




class Register(View):
    form_class = RegisterForm
    template_name = "auth/register.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            messages.success(request,
                             "your account has been created successfully")
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.user_type == 'guest':
                        return redirect('/resturant')
                    elif user.user_type == 'admin':
                        return redirect('/dashboard')
        return render(request, self.template_name, {'form': form})


class Login(View):
    """ Login View."""
    form_class = LoginForm
    template_name = "auth/login.html"

    def get(self, request):
        logout(request)
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            messages.success(request, "you have logged in successfully ")
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/dashboard')
            else:
                error = "username or password is incorrect"
        return render(
            request, self.template_name, {'form': form, 'error': error})


class LogoutView(View):
    """ Custom Logout View."""
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login')



@login_required(login_url="/login/")
def dashboard(request):
    """Admin dashboard view."""
    reservations = Reservation.objects.order_by('-id').all()
    users = User.objects.all()
    orderitem = OrderItem.objects.order_by('-id').all()
    price = 0
    for i in orderitem:
        if i.order.paid == 1:
            price += Decimal(i.price)*Decimal(i.quantity)
    order_pending = OrderItem.objects.filter(status="pending")
    order_confirmed = OrderItem.objects.filter(status="confirmed")
    pending = Reservation.objects.filter(status="pending")
    confirmed = Reservation.objects.filter(status="confirmed")
    webpush = {"group": 'webadmin'}

    return render(request, "super/dashboard.html",
                  {'users': users,
                  'orderitem' : orderitem,
                   'reservations': reservations,
                   'order_pending' : order_pending,
                   'order_confirmed' : order_confirmed,
                   'price': price, 
                   'pending': pending, 'confirmed': confirmed, 'webpush': webpush})


    
@login_required
def order_delete(request, pk):
    order = OrderItem.objects.get(id=pk)
    order.delete()
    return redirect('/dashboard', messages.success(request, 'Order was successfully deleted.', 'alert-success'))

@login_required
def reservation_delete(request, pk):
    reserve = Reservation.objects.get(id=pk)
    reserve.delete()
    return redirect('/dashboard', messages.success(request, 'Reservation was  successfully deleted.', 'alert-success'))




@login_required
def show(request, order_id):
    order = OrderItem.objects.filter(order_id=order_id).first()
    items = OrderItem.objects.filter(order_id=order_id)
    price = 0
    for i in items:
        price += Decimal(i.price)*Decimal(i.quantity)
    return render(request, 'super/show.html', {'order': order, 'items': items, 'price':price})


class AddReservation(LoginRequiredMixin, CreateView):
    """Admin user add new reservation."""
    template_name = "super/new_reserve.html"
    form_class = ReservationForm
    login_url = '/login/'

    def form_valid(self, form):
        new = form.save(commit=False)
        new.save()
        # send a flash message to the user
        messages.success(
            self.request,
            "you have successfully added a new table reservation ")
        # redirect the user back to his/her dashboard
        return redirect("/dashboard")


class AddItem(LoginRequiredMixin, CreateView):
    """Admin user add new reservation."""
    template_name = "super/new_item.html"
    form_class = MenuForm
    login_url = '/login/'

    def form_valid(self, form):
        new = form.save(commit=False)
        new.save()
        # send a flash message to the user
        messages.success(
            self.request,
            "you have successfully added a new item ")
        # redirect the user back to his/her dashboard
        return redirect("/dashboard")

class AddFeedback(LoginRequiredMixin, CreateView):
    """Admin user add new reservation."""
    template_name = "super/new_feedback.html"
    form_class = FeedbackForm
    login_url = '/login/'

    def form_valid(self, form):
        new = form.save(commit=False)
        new.save()
        # send a flash message to the user
        messages.success(
            self.request,
            "you have successfully submitted Your Feedback !, Thankyou")
        # redirect the user back to his/her dashboard
        return redirect("/")


class UpdateMenuItem(LoginRequiredMixin, UpdateView):
    """Admin user updates all the reservation."""
    form_class = MenuForm
    template_name = "super/new_item.html"
    model = MenuItem

    def get_object(self, *args, **kwargs):
        obj = get_object_or_404(MenuItem, pk=self.kwargs['pk'])
        return obj

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, "you have successfully updated the MenuItem")
        return redirect('/view-menuitems')


class UpdateReservation(LoginRequiredMixin, UpdateView):
    """Admin user updates all the reservation."""
    form_class = ReservationUpdateForm
    template_name = "super/update_reserve.html"
    model = Reservation

    def get_object(self, *args, **kwargs):
        obj = get_object_or_404(Reservation, pk=self.kwargs['pk'])
        return obj

    def form_valid(self, form):
        val = form.cleaned_data['status']
        form.save()
        messages.success(
            self.request, "you have successfully updated the reservation")
        if val == "confirmed":
            return redirect('orders:reservation_status', pk=self.kwargs['pk'])
        return redirect('/dashboard')


@login_required(login_url="/login/")
def view_reservations(request):
    """Admin user view all the reservations."""
    reservations = Reservation.objects.all()
    return render(request,
                  "super/view_reserve.html",
                  {'reservations': reservations})


@login_required(login_url="/login/")
def view_menuitems(request):
    """Admin user view all the reservations."""
    menuitem = MenuItem.objects.all()
    return render(request,
                  "super/view_items.html",
                  {'menuitem': menuitem})
