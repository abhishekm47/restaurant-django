from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField
# Create your models here.


class User(AbstractUser):
    website = models.URLField(blank=True)
    phone_number = models.CharField(max_length=12)
    picture = models.ImageField(blank=True)
    bio = models.CharField(max_length=300)


class Reservation(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField(blank=True)
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    six = '6'
    seven = '7'
    eight = '8'
    nine = '9'
    ten = '10'
    eleven = '11'
    twelve = '12'
    thirteen = '13'
    fourteen = '14'
    fifthen = '15'
    sixteen = '16'
    seventeen = '17'
    eighteen = '18'
    nineteen = '19'
    twenty = '20'
    people_choices = (
        (one, '1'), (two, '2'),
        (three, '3'), (four, '4'), (five, '5'), (six, '6'), (seven, '7'), (eight, '8'), (nine, '9'),
        (ten, '10'), (eleven, '11'), (twelve, '12'), (thirteen, '13'), (fourteen, '14'), (fifthen, '15'),
         (sixteen, '16'), (seventeen, '17'), (eighteen, '18'), (nineteen, '19'), (twenty, '20')
    )
    people = models.CharField(
        max_length=3, choices=people_choices, default=two)
    resto1 = "Amsterdamseweg 114 Next to Molen, 1182 HH, Amstelveen The Netherlands"
    resto2 = "Piet Mondriaanplein 189-193, 3812 GZ Amersfoort, The Netherlands"
    resto_choices = ((resto1, "Amsterdamseweg 114 Next to Molen, 1182 HH, Amstelveen The Netherlands"),(resto2, "Piet Mondriaanplein 189-193, 3812 GZ Amersfoort, The Netherlands") )
    resto_type = models.CharField(
        max_length=400, choices=resto_choices, default=resto1)
    time = models.TimeField()
    date_reserved = models.DateField()
    date_booked = models.DateTimeField(auto_now_add=True)
    pending = "pending"
    confirmed = "confirmed"
    status_choices = ((pending, "pending"), (confirmed, "confirmed"))
    status = models.CharField(
        max_length=22, choices=status_choices, default=pending)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.first_name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    cost = MoneyField(max_digits=50, decimal_places=2, default_currency='EUR')
    description = models.TextField()
    dutch_description = models.TextField()
    image = models.ImageField(blank=True)
    time = models.TimeField(auto_now_add=True)
    available = "available"
    unavailable = "unavailable"
    status_choices = ((available, "available"), (unavailable, "unavailable"))
    status = models.CharField(
        max_length=22, choices=status_choices, default=available)
    takeaway = "Takeaway"
    home = "Home Delivery"
    type_choices = ((takeaway, "Takeaway"), (home, "Home Delivery"))
    Menu_type =models.CharField(
        max_length=100, choices=type_choices, default=home) 
    Soepen = "Soepen"
    Nepali_menu = "Nepali Menu"
    Voorgerechten = "Voorgerechten"
    Momo_gerechten = "Momo gerechten"
    Noodle_gerechten = "Noodle gerechten"
    Tandoori_gerechten = "Tandoori gerechten"
    Kipgerechten = "Kipgerechten"
    Lamsgerechten = "Lamsgerechten"
    Zeevruchten_gerechten = "Zeevruchten gerechten"
    Vegetarische_gerechten = "Vegetarische gerechten"
    Biryani_gerechten = "Biryani gerechten"
    Extra = "Extra's"
    Indiaas_brood = "Indiaas brood"
    Nagerechten = "Nagerechten"
    Dranken = "Dranken"
    category_choices = ((Soepen, "Soepen"), (Voorgerechten, "Voorgerechten"), (Momo_gerechten, "Momo gerechten"),(Nepali_menu, "Nepali Menu"),
                        (Noodle_gerechten, "Noodle gerechten"), (Tandoori_gerechten, "Tandoori gerechten"), (Kipgerechten, "Kipgerechten"), (Lamsgerechten, "Lamsgerechten"), (Zeevruchten_gerechten, "Zeevruchten gerechten"),
                        (Vegetarische_gerechten, "Vegetarische gerechten"), ( Biryani_gerechten, "Biryani gerechten"), (Extra, "Extra's"), ( Indiaas_brood, "Indiaas brood"), (Nagerechten, "Nagerechten"), (Dranken, "Dranken"))
    category = models.CharField(
        max_length=30, choices=category_choices, default=available)
    def __str__(self):
        return '%s - %s' % (self.name, self.cost)

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rate = models.CharField(max_length=22)
    rate_2 = models.CharField(max_length=22)

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField(blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField(max_length=1000)
    date_sent = models.DateTimeField(auto_now_add=True)

